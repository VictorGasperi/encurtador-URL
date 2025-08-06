from abc import ABC, abstractmethod
from typing import Optional

from app.modules.url_management.domain.entities.short_url import ShortUrl


class IUrlRepository(ABC):

    @abstractmethod
    def create_url(self, short_url: ShortUrl) -> ShortUrl:
        '''
        Create a url record and returns it
        '''
    pass

    @abstractmethod
    def get_url(self, code: str) -> Optional[ShortUrl]:
        '''
        Given the URL code, returns the correspondent ShortURL
        '''
    pass

    @abstractmethod
    def code_exists(self, code: str) -> bool:
        '''
        Given the URL code, returns if it already exists
        '''
    pass