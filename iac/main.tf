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
  name = "lambda-role-${var.stage}"

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
  name = "lambda-policy-${var.stage}"

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

resource "aws_lambda_function" "app" {
  function_name = "url-shortener-lambda-${var.stage}"
  role          = aws_iam_role.lambda_exec_role.arn
  package_type  = "Image"
  image_uri     = var.lambda_image_uri

  timeout = 10

  tags = {
    Project = var.project_name
    Stage = var.stage
  }
}