output "ecr-URL" {
  value = aws_ecr_repository.us-ecr.repository_url
}

output "api-link" {
  value = aws_apigatewayv2_stage.apigw-deploy.invoke_url
}