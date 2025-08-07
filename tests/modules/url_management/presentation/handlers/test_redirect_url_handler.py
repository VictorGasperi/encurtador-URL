from fastapi import HTTPException
import pytest
from app.modules.url_management.application.redirect_url_usecase import RedirectUrlUsecase
from app.modules.url_management.infrastructure.repositories.url_repository_mock import UrlRepositoryMock
from app.modules.url_management.presentation.handlers.redirect_url_handler import RedirectUrlHandler


class TestRedirectUrlHandler():

    def test_redirect_url_handler(self):
        repo = UrlRepositoryMock()
        usecase = RedirectUrlUsecase(repo)
        handler = RedirectUrlHandler(usecase)

        code = "qwerty"

        response = handler(code)

        assert response == 'https://anotherdomain.com/home'

    def test_redirect_url_handler_with_invalid_code(self):
        repo = UrlRepositoryMock()
        usecase = RedirectUrlUsecase(repo)
        handler = RedirectUrlHandler(usecase)

        code = "98765524"

        with pytest.raises(HTTPException) as e:
            handler(code)

        assert e.value.status_code == 422

    def test_redirect_url_handler_with_unexistent_code(self):
        repo = UrlRepositoryMock()
        usecase = RedirectUrlUsecase(repo)
        handler = RedirectUrlHandler(usecase)

        code = "fedcba"

        with pytest.raises(HTTPException) as e:
            handler(code)

        assert e.value.status_code == 404

