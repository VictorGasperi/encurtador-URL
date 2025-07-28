# Imagem base do AWS Lambda para Python
FROM public.ecr.aws/lambda/python:3.11

# Copiar dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar app
COPY app app/

# Definir handler padrão do Lambda
CMD ["app.main.handler"]
