from typing import List
from app.modules.url_management.domain.entities.short_url import ShortURL
from app.modules.url_management.domain.repositories.url_repository import IURLRepository


class URLRepositoryMock(IURLRepository):
    urls: List[ShortURL]

    def __init__(self):
        self.urls = [
            ShortURL(code='123456', original_url='https://example.com/page1'),
            ShortURL(code='abcdef', original_url='https://example.com/page2'),
            ShortURL(code='qwerty', original_url='https://anotherdomain.com/home'),
        ]

        # TODO: terminar o mock