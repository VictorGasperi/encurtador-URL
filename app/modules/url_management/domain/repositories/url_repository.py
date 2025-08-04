from abc import ABC, abstractmethod

from app.modules.url_management.domain.entities.short_url import ShortURL


class IURLRepository(ABC):

    @abstractmethod
    def create_url(self, url: str) -> ShortURL:
        '''
        Given an URL, creates a code for it
        '''
    pass