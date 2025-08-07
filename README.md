# 🔗 Encurtador de URL

Este projeto é um encurtador de URLs simples e eficiente, que permite gerar códigos curtos a partir de URLs originais e redirecionar usuários para o link encurtado. A aplicação é desenvolvida em Python utilizando FastAPI com deploy em AWS Lambda via imagem Docker, seguindo uma arquitetura monolítica modular orientada a DDD (Domain-Driven Design).

## 🎯 Objetivo

Oferecer uma API enxuta para:
- POST /url/shorten: Recebe uma URL original e retorna um código encurtado.
- GET /url/redirect/{code}: Redireciona para a URL original associada ao código fornecido.

## 🛠️ Tecnologias Utilizadas

### Backend
- 🐍 Python
- ⚡ FastAPI
- 🪝 Mangum (adaptador ASGI para AWS Lambda)

### Infraestrutura
- 🧱 Terraform (Infraestrutura como Código - IaC)
- 🪂 AWS Lambda (deploy via Docker container)
- 🚪 Amazon API Gateway
- 🗃️ Amazon DynamoDB (armazenamento das URLs)
- 📦 Amazon ECR (repositório de imagens Docker)

### Outros
- 🐳 Docker (container da aplicação)
- 🧪 Pytest (testes unitários)
- 🔄 GitHub Actions (CI/CD)

## 🏗️ Infraestrutura

A infraestrutura é provisionada com Terraform e inclui:
- 📦 Repositório ECR para armazenar a imagem Docker do backend.
- 🪂 Função Lambda configurada para executar a imagem.
- 🚪 API Gateway integrado à Lambda.
- 🗃️ Tabela DynamoDB com suporte a TTL.
- ☁️ Backend remoto para o Terraform (via S3).

## 🚀 Como Inicializar o Projeto

### ✅ Pré-requisitos

- Secrets e Variables do Github definidos.

### 📄 Variáveis necessárias

.env (para rodar os testes locais):
STAGE=test

## 🧪 Testes Locais

1. Crie um ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows

2. Instale as dependências:
   pip install -r requirements.txt

3. Configure o arquivo .env com:
   STAGE=test

4. Execute os testes:
   pytest tests/

## 🚢 Deploy com Terraform + GitHub Actions

O deploy é feito automaticamente pelo pipeline de CD quando há push na branch prod. Isso é configurável no workflow, podendo habilitar para outras branches. O workflow realiza:
- Build e push da imagem para o ECR.
- Execução do terraform apply para provisionar os recursos e atualizar a Lambda com a nova imagem.

### 🔐 Secrets no GitHub
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

### 🧩 Vars no GitHub
- AWS_REGION
- BUCKET_NAME (bucket S3 com backend remoto do Terraform)

## 📁 Estrutura do Projeto

```bash
.
├── .github/workflows/         CI/CD com GitHub Actions
├── app/                       Código principal da aplicação FastAPI
│   └── modules/               Camadas organizadas por DDD
│   └── shared/                Arquivos compartilhados entre módulos
│   └── main.py                Ponto de entrada do Lambda  
├── iac/                       Arquivos Terraform (Infraestrutura como Código)
├── tests/                     Testes automatizados com Pytest
├── Dockerfile                 Build da imagem do container
└── requirements.txt           Dependências Python
```

## 📌 Observações

- A aplicação não é executável localmente via FastAPI — apenas via testes unitários.
- O Mangum adapta a aplicação ASGI para Lambda, sendo o FastAPI responsável pelo roteamento.

## 🧾 Convenções de Nomeação

Todos os recursos criados na AWS (como ECR, Lambda, DynamoDB e API Gateway) utilizam o nome do projeto como base — que, por convenção, é o mesmo nome do repositório GitHub.

As branches representam os diferentes estágios do projeto (dev, homol, prod). Esse valor de stage é usado como sufixo na criação dos recursos, por exemplo:

- Branch `homol` ➝ recursos como `encurtador-url-dynamodb-homol`
- Branch `prod` ➝ recursos como `encurtador-url-lambda-prod`

Essa configuração é feita automaticamente no pipeline de CD ao dar push ou merge na branch correspondente.


### 💬 Por favor, deixe sua recomendação como Issue

