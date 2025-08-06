from app.modules.url_management.domain.exceptions import InvalidCodeException, UrlNotFoundException
from app.modules.url_management.domain.repositories.url_repository import IUrlRepository


class RedirectUrlUsecase():
    def __init__(self, url_repository: IUrlRepository):
        self.url_repository = url_repository

    def __call__(self, code: str) -> str:

        if len(code) != 6:
            raise InvalidCodeException(code)
        
        if not self.url_repository.code_exists(code):
            raise UrlNotFoundException(code)
        
        response = self.url_repository.get_url(code)

        return response.original_url
        
