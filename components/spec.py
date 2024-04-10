SPEC = {
    "openapi": "3.0.1",
    "paths": {
        "/login": {
            "post": {
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AuthModel"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "passthroughBehavior": "when_no_match",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "options": {
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Methods": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Headers": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Empty"
                                }
                            }
                        }
                    }
                },
                "x-amazon-apigateway-integration": {
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Methods": "'OPTIONS,POST'",
                                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\"statusCode\": 200}"
                    },
                    "passthroughBehavior": "when_no_match",
                    "type": "mock"
                }
            }
        },
        "/chat_history": {
            "get": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "500": {
                        "description": "500 response",
                        "content": {}
                    },
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        },
                        "Internal.*": {
                            "statusCode": "500",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"Authorization\": \"$input.params('Authorization')\"\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "post": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/CreateChatModel"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "500": {
                        "description": "500 response",
                        "content": {}
                    },
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        },
                        "Internal.*": {
                            "statusCode": "500",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"Authorization\": \"$input.params('Authorization')\",\n    \"chats\": $input.json('$')\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "delete": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "500": {
                        "description": "500 response",
                        "content": {}
                    },
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        },
                        "Internal.*": {
                            "statusCode": "500",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"Authorization\": \"$input.params('Authorization')\"\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "options": {
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Methods": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Headers": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Empty"
                                }
                            }
                        }
                    }
                },
                "x-amazon-apigateway-integration": {
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Methods": "'GET,OPTIONS,POST'",
                                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\"statusCode\": 200}"
                    },
                    "passthroughBehavior": "when_no_match",
                    "type": "mock"
                }
            }
        },
        "/expenses/{id}": {
            "get": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }, {
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "404": {
                        "description": "404 response",
                        "content": {}
                    },
                    "500": {
                        "description": "500 response",
                        "content": {}
                    },
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "Entity.*": {
                            "statusCode": "404",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        },
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        },
                        "Internal.*": {
                            "statusCode": "500",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"pathParameters\": {\n        \"id\": $input.params('id')\n    },\n    \"Authorization\": \"$input.params('Authorization')\"\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "put": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }, {
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/ExpenseModel"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "500": {
                        "description": "500 response",
                        "content": {}
                    },
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        },
                        "Internal.*": {
                            "statusCode": "500",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"pathParameters\": {\n        \"id\": $input.params('id')\n    },\n    \"Authorization\": \"$input.params('Authorization')\",\n    \"expense\": $input.json('$')\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "delete": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }, {
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "500": {
                        "description": "500 response",
                        "content": {}
                    },
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        },
                        "Internal.*": {
                            "statusCode": "500",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"pathParameters\": {\n        \"id\": $input.params('id')\n    },\n    \"Authorization\": \"$input.params('Authorization')\"\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "options": {
                "parameters": [{
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Methods": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Headers": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Empty"
                                }
                            }
                        }
                    }
                },
                "x-amazon-apigateway-integration": {
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Methods": "'DELETE,GET,OPTIONS,PUT'",
                                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\"statusCode\": 200}"
                    },
                    "passthroughBehavior": "when_no_match",
                    "type": "mock"
                }
            }
        },
        "/expense_categories/{id}": {
            "get": {
                "parameters": [{
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "404": {
                        "description": "404 response",
                        "content": {}
                    },
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "Entity.*": {
                            "statusCode": "404",
                            "responseTemplates": {
                                "application/json": "{\n    \"error\": $input.json('$.errorMessage')\n}"
                            }
                        },
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"pathParameters\": {\n        \"id\": $input.params('id')\n    }\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "options": {
                "parameters": [{
                    "name": "id",
                    "in": "path",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Methods": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Headers": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Empty"
                                }
                            }
                        }
                    }
                },
                "x-amazon-apigateway-integration": {
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Methods": "'GET,OPTIONS'",
                                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\"statusCode\": 200}"
                    },
                    "passthroughBehavior": "when_no_match",
                    "type": "mock"
                }
            }
        },
        "/expenses": {
            "get": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"Authorization\": \"$input.params('Authorization')\"\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "post": {
                "parameters": [{
                    "name": "Authorization",
                    "in": "header",
                    "required": True,
                    "schema": {
                        "type": "string"
                    }
                }],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/ExpenseModel"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "201": {
                        "description": "201 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body, query string parameters, and headers",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "201",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\n    \"expense\": $input.json('$'),\n    \"Authorization\": \"$input.params('Authorization')\"\n}"
                    },
                    "passthroughBehavior": "when_no_templates",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "options": {
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Methods": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Headers": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Empty"
                                }
                            }
                        }
                    }
                },
                "x-amazon-apigateway-integration": {
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Methods": "'GET,OPTIONS,POST'",
                                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\"statusCode\": 200}"
                    },
                    "passthroughBehavior": "when_no_match",
                    "type": "mock"
                }
            }
        },
        "/register": {
            "post": {
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AuthModel"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-request-validator": "Validate body",
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "passthroughBehavior": "when_no_match",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "options": {
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Methods": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Headers": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Empty"
                                }
                            }
                        }
                    }
                },
                "x-amazon-apigateway-integration": {
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Methods": "'OPTIONS,POST'",
                                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\"statusCode\": 200}"
                    },
                    "passthroughBehavior": "when_no_match",
                    "type": "mock"
                }
            }
        },
        "/expense_categories": {
            "get": {
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {}
                    }
                },
                "x-amazon-apigateway-integration": {
                    "httpMethod": "POST",
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "passthroughBehavior": "when_no_match",
                    "contentHandling": "CONVERT_TO_TEXT",
                    "type": "aws"
                }
            },
            "options": {
                "responses": {
                    "200": {
                        "description": "200 response",
                        "headers": {
                            "Access-Control-Allow-Origin": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Methods": {
                                "schema": {
                                    "type": "string"
                                }
                            },
                            "Access-Control-Allow-Headers": {
                                "schema": {
                                    "type": "string"
                                }
                            }
                        },
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Empty"
                                }
                            }
                        }
                    }
                },
                "x-amazon-apigateway-integration": {
                    "responses": {
                        "default": {
                            "statusCode": "200",
                            "responseParameters": {
                                "method.response.header.Access-Control-Allow-Methods": "'GET,OPTIONS'",
                                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                                "method.response.header.Access-Control-Allow-Origin": "'*'"
                            }
                        }
                    },
                    "requestTemplates": {
                        "application/json": "{\"statusCode\": 200}"
                    },
                    "passthroughBehavior": "when_no_match",
                    "type": "mock"
                }
            }
        }
    },
    "components": {
        "schemas": {
            "Empty": {
                "title": "Empty Schema",
                "type": "object"
            },
            "AuthModel": {
                "title": "AuthModel",
                "required": ["password", "username"],
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string"
                    },
                    "password": {
                        "type": "string"
                    }
                }
            },
            "CreateChatModel": {
                "title": "CreateChatModel",
                "required": ["chats"],
                "type": "object",
                "properties": {
                    "chats": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "role_id": {
                                    "maximum": 3,
                                    "minimum": 1,
                                    "type": "integer"
                                },
                                "content": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            },
            "ExpenseModel": {
                "title": "ExpenseModel",
                "required": ["exp_category_id", "expense_amount", "expense_name", "month_year"],
                "type": "object",
                "properties": {
                    "expense_name": {
                        "type": "string"
                    },
                    "expense_amount": {
                        "minimum": 0,
                        "type": "number"
                    },
                    "month_year": {
                        "type": "string"
                    },
                    "exp_category_id": {
                        "minimum": 0,
                        "type": "integer"
                    }
                }
            }
        }
    },
    "x-amazon-apigateway-gateway-responses": {
        "DEFAULT_4XX": {
            "responseParameters": {
                "gatewayresponse.header.Access-Control-Allow-Methods": "'GET,OPTIONS,POST'",
                "gatewayresponse.header.Access-Control-Allow-Origin": "'*'",
                "gatewayresponse.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'"
            }
        },
        "DEFAULT_5XX": {
            "responseParameters": {
                "gatewayresponse.header.Access-Control-Allow-Methods": "'GET,OPTIONS,POST'",
                "gatewayresponse.header.Access-Control-Allow-Origin": "'*'",
                "gatewayresponse.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'"
            }
        }
    },
    "x-amazon-apigateway-request-validators": {
        "Validate body": {
            "validateRequestParameters": False,
            "validateRequestBody": True
        },
        "Validate body, query string parameters, and headers": {
            "validateRequestParameters": True,
            "validateRequestBody": True
        }
    }
}
