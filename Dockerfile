FROM public.ecr.aws/lambda/python:3.11

ARG STAGE
ARG DYNAMO_TABLE_NAME


ENV STAGE=$STAGE
ENV DYNAMO_TABLE_NAME=$DYNAMO_TABLE_NAME


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY app app/


CMD ["app.main.handler"]
