import pytest
from app.modules.url_management.application.redirect_url_usecase import RedirectUrlUsecase
from app.modules.url_management.domain.exceptions import InvalidCodeException, UrlNotFoundException
from app.modules.url_management.infrastructure.repositories.url_repository_mock import UrlRepositoryMock


class TestRedirectUrlUsecase():

    def test_redirect_url_usecase(self):
        repo = UrlRepositoryMock()
        usecase = RedirectUrlUsecase(repo)

        response = usecase('abcdef')

        assert response == 'https://example.com/page2'

    def test_redirect_url_with_invalid_code(self):
        repo = UrlRepositoryMock()
        usecase = RedirectUrlUsecase(repo)

        with pytest.raises(InvalidCodeException):
            response = usecase('123456789')

    def test_redirect_url_with_unexistent_code(self):
        repo = UrlRepositoryMock()
        usecase = RedirectUrlUsecase(repo)

        with pytest.raises(UrlNotFoundException):
            response = usecase('fedcba')
