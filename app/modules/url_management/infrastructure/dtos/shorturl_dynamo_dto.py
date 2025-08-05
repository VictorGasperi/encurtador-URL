from datetime import datetime
from app.modules.url_management.domain.entities.short_url import ShortUrl
from app.shared.environments import Environments


class ShortUrlDynamoDTO():

    @staticmethod
    def to_dynamo(short_url: ShortUrl) -> dict:
        item = {
            'PK': f"URL#{short_url.code}",
            'original_url': short_url.original_url,
            'created_at': short_url.created_at.isoformat()
        }
        if short_url.ttl:
            item['TTL'] = short_url.ttl

        return item
    
    @staticmethod
    def to_entity(item: dict) -> ShortUrl:
        return ShortUrl(
            code=str(item['PK']).replace('URL#', ''),
            original_url=str(item['original_url']),
            created_at=datetime.fromisoformat(item['created_at']),
            ttl=int(item.get('TTL'))
        )