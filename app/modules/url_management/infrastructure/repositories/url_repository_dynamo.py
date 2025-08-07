from typing import Optional
import boto3
from app.modules.url_management.domain.entities.short_url import ShortUrl
from app.modules.url_management.domain.repositories.url_repository import IUrlRepository
from app.modules.url_management.infrastructure.dtos.shorturl_dynamo_dto import ShortUrlDynamoDTO
from app.shared.environments import Environments


class UrlRepositoryDynamo(IUrlRepository):

    tablename = Environments.get_envs().dynamo_table_name

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.tablename)

    def create_url(self, short_url: ShortUrl) -> ShortUrl:

        dynamodb_item = ShortUrlDynamoDTO.to_dynamo(short_url)
        self.table.put_item(Item=dynamodb_item)

        return short_url
    
    def get_url(self, code: str) -> Optional[ShortUrl]:
        response = self.table.get_item(Key={'PK': f'URL#{code}'})
        item = ShortUrlDynamoDTO.to_entity(response["Item"])
        if not item:
            return None
        return item
    
    def code_exists(self, code: str) -> bool:
        response = self.table.get_item(
            Key={
                'PK': f'URL#{code}'
            },
            ProjectionExpression='PK'
        )
        return 'Item' in response
