variable "stage" {
  type        = string
  description = "Ambiente de deploy (dev, homol, prod)"
}

variable "aws_region" {
  type = string
  description = "Regiao de deploy"
}

variable "aws_access_key" {
  type = string
  description = "Chave de acesso"
}

variable "aws_secret_key" {
  type = string
  description = "Chave de segredo"
}

variable "project_name" {
  type        = string
  description = "Nome base do projeto"
}

variable "lambda_image_uri" {
  type = string
  description = "URI para a imagem anexada ao lambda"
}