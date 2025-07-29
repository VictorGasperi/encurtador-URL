resource "aws_ecr_repository" "us-ecr" {
  name                 = "${var.project_name}-ecr"
  image_tag_mutability = "MUTABLE"
  force_delete = true
  tags = {
    Project = var.project_name
    Stage = var.stage
  }
}

# Permissão para que a funcao lambda possa assumir uma role. Utiliza uma "Trust policy"
resource "aws_iam_role" "lambda_exec_role" {
  name = "${var.project_name}-lambda-role-${var.stage}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
  tags = {
    Project = var.project_name
    Stage = var.stage
  }
}


# Qual a role que o lambda vai assumir. Utiliza uma "IAM policy"

resource "aws_iam_policy" "lambda_policy" {
  name = "${var.project_name}-lambda-policy-${var.stage}"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem"
        ],
        Resource = "arn:aws:dynamodb:us-east-1:123456789012:table/url-shortener-table-${var.stage}"
      },
      {
        Effect = "Allow",
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "*"
      }
    ]
  })
  tags = {
    Project = var.project_name
    Stage = var.stage
  }
}

# Utilizado para anexar ambas as politicas a funcao lambda

resource "aws_iam_role_policy_attachment" "lambda_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}

# Criacao da funcao lambda

resource "aws_lambda_function" "lambda-app" {
  function_name = "${var.project_name}-lambda-${var.stage}"
  role          = aws_iam_role.lambda_exec_role.arn
  package_type  = "Image"
  image_uri     = var.lambda_image_uri

  timeout = 10

  tags = {
    Project = var.project_name
    Stage = var.stage
  }
}

resource "aws_dynamodb_table" "database" {
  name           = "${var.project_name}-dynamodb-${var.stage}"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "code"

  attribute {
    name = "code"
    type = "S"
  }

  ttl {
    attribute_name = "TTL"
    enabled        = true
  }

  tags = {
    Project = var.project_name
    Stage = var.stage
  }

}

resource "aws_apigatewayv2_api" "apigw" {
  name          = "${var.project_name}-apigwv2-${var.stage}"
  protocol_type = "HTTP"
  tags = {
    Project = var.project_name
    Stage = var.stage
  }
}

resource "aws_apigatewayv2_integration" "apigw-lambda" {
  api_id                = aws_apigatewayv2_api.apigw.id
  integration_type      = "AWS_PROXY"
  integration_method    = "POST"
  integration_uri       = aws_lambda_function.lambda-app.invoke_arn
}

resource "aws_apigatewayv2_route" "decouple-apigw-routes" {
  api_id    = aws_apigatewayv2_api.apigw.id
  route_key = "ANY /{proxy+}"
  target = "integrations/${aws_apigatewayv2_integration.apigw-lambda.id}"
}

resource "aws_apigatewayv2_stage" "apigw-deploy" {
  api_id = aws_apigatewayv2_api.apigw.id
  name   = var.stage
  auto_deploy = true
  tags = {
    Project = var.project_name
    Stage = var.stage
  }
}

# Permissão para que o APIGW invoque o lambda

resource "aws_lambda_permission" "allow-apigw-lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda-app.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.apigw.execution_arn}/*/*"
}