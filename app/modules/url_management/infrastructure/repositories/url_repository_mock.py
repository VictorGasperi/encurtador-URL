from typing import List, Optional
from app.modules.url_management.domain.entities.short_url import ShortUrl
from app.modules.url_management.domain.exceptions import UrlNotFoundException
from app.modules.url_management.domain.repositories.url_repository import IUrlRepository
from app.shared.utils.generate_random_code import generate_random_code

class UrlRepositoryMock(IUrlRepository):
    urls: List[ShortUrl]

    def __init__(self):
        self.urls = [
            ShortUrl(code='123456', original_url='https://example.com/page1'),
            ShortUrl(code='abcdef', original_url='https://example.com/page2'),
            ShortUrl(code='qwerty', original_url='https://anotherdomain.com/home'),
        ]

    def create_url(self, short_url: ShortUrl) -> ShortUrl:
        self.urls.append(short_url)     
        return short_url   
    
    def get_url(self, code) -> Optional[ShortUrl]:
        
        for url in self.urls:
            if url.code == code:
                return url
        raise UrlNotFoundException(code)
        
    def code_exists(self, code: str) -> bool:
        if code in [url.code for url in self.urls]: return True
        else: return False
