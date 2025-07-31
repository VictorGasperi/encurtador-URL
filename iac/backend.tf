terraform {
  backend "s3" {
    bucket = "gasp-terraform-backend-state"
    key    = "url_shortener/terraform.tfstate"
    region = "us-east-2"
    encrypt = true
  }
}