from app.modules.url_management.domain.entities.short_url import ShortUrl
from app.modules.url_management.domain.repositories.url_repository import IUrlRepository
from app.modules.url_management.domain.exceptions import InvalidUrlException
from app.shared.utils.generate_random_code import generate_random_code


class ShortenUrlUsecase():

    def __init__(self, url_repository: IUrlRepository):
        self.url_repository = url_repository

    def __call__(self, original_url: str) -> ShortUrl:

        if original_url == '' or original_url is None:
            raise InvalidUrlException(original_url)

        code = generate_random_code(6)
        while self.url_repository.code_exists(code):
            code = generate_random_code(6)

        short_url = ShortUrl(code, original_url)
        self.url_repository.create_url(short_url)
        return short_url