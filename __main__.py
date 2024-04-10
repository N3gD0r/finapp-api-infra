from components import SPEC
from pulumi.resource import ResourceOptions
from pulumi.runtime.sync_await import _sync_await

import json
import os
import pulumi
import pulumi_aws as aws


PRJ = os.getenv('PULUMI_PRJ')
STACK = os.getenv('PULUMI_STACK')


def set_integration_uris(uris: dict, body: dict):
    api_spec = dict(body)
    paths = api_spec['paths']

    paths['/login']['post']['x-amazon-apigateway-integration']['uri'] = uris['login']
    paths['/register']['post']['x-amazon-apigateway-integration']['uri'] = uris['register']

    paths['/expense_categories']['get']['x-amazon-apigateway-integration']['uri'] = uris['get_categories']
    paths['/expense_categories/{id}']['get']['x-amazon-apigateway-integration']['uri'] = uris['get_category']

    paths['/chat_history']['get']['x-amazon-apigateway-integration']['uri'] = uris['get_chat_history']
    paths['/chat_history']['post']['x-amazon-apigateway-integration']['uri'] = uris['post_chat_history']
    paths['/chat_history']['delete']['x-amazon-apigateway-integration']['uri'] = uris['delete_chats']

    paths['/expenses']['get']['x-amazon-apigateway-integration']['uri'] = uris['get_expenses']
    paths['/expenses']['post']['x-amazon-apigateway-integration']['uri'] = uris['post_expense']

    paths['/expenses/{id}']['get']['x-amazon-apigateway-integration']['uri'] = uris['get_expense']
    paths['/expenses/{id}']['put']['x-amazon-apigateway-integration']['uri'] = uris['update_expense']
    paths['/expenses/{id}']['delete']['x-amazon-apigateway-integration']['uri'] = uris['delete_expense']
    return api_spec


def main():
    stack_ref = pulumi.StackReference(f"{PRJ}/{STACK}")
    invoke_uris: dict = _sync_await(stack_ref.get_output_details('lambdas')).value
    lambda_arns: dict = _sync_await(stack_ref.get_output_details('lambda_arns')).value
    methods: dict = _sync_await(stack_ref.get_output_details('methods')).value

    api_spec = set_integration_uris(uris=invoke_uris, body=SPEC)

    rest_api_gateway = aws.apigateway.RestApi(
        resource_name="rest-api-gateway",
        name="ai-budget-api",
        description="API Gateway for personal budget AI",
        body=json.dumps(api_spec),
    )

    api_gateway_deployment = aws.apigateway.Deployment(
        resource_name="api-deployment",
        rest_api=rest_api_gateway.id,
        opts=ResourceOptions(depends_on=[rest_api_gateway])
    )

    api_stage = aws.apigateway.Stage(
        resource_name="api-stage-dev",
        rest_api=rest_api_gateway.id,
        deployment=api_gateway_deployment.id,
        stage_name="dev",
        opts=ResourceOptions(depends_on=[rest_api_gateway, api_gateway_deployment])
    )

    perms = []
    for key, value in lambda_arns.items():
        lambda_permission = aws.lambda_.Permission(
            resource_name=f"lambda-permission-{key[:-4]}",
            statement_id=f"AllowExecutionFromApiGateway-{key[:-4]}",
            action="lambda:InvokeFunction",
            function=value,
            principal="apigateway.amazonaws.com",
            source_arn=rest_api_gateway.execution_arn.apply(lambda arn: f"{arn}/dev/{methods[key]}"),
            opts=ResourceOptions(depends_on=[rest_api_gateway])
        )
        perms.append(lambda_permission.statement_id)

    pulumi.export("rest_api_arn", rest_api_gateway.arn)
    pulumi.export("rest_api", rest_api_gateway.execution_arn)
    pulumi.export("api_deploy", api_gateway_deployment.id)
    pulumi.export("api_stage_arn", api_stage.arn)
    pulumi.export("api_stage", api_stage.stage_name)
    pulumi.export("api_stage_url", api_stage.invoke_url)
    pulumi.export("lambda_permissions", perms)


if __name__ == "__main__":
    main()

