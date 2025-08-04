from fastapi import HTTPException
import pytest
from app.modules.url_management.application.shorten_url_usecase import ShortenUrlUsecase
from app.modules.url_management.infrastructure.repositories.url_repository_mock import UrlRepositoryMock
from app.modules.url_management.presentation.handlers.shorten_url_handler import ShortenUrlHandler


class TestShortenUrlHandler():

    def test_shorten_url_handler(self):
        repo = UrlRepositoryMock()
        usecase = ShortenUrlUsecase(repo)
        handler = ShortenUrlHandler(usecase)

        body = {
            "original_url": "test-123"
        }

        response = handler(body)

        assert response.get('original_url') == body.get('original_url')
        assert len(response.get('code')) == 6

    def test_shorten_url_handler_invalid_url(self):
        repo = UrlRepositoryMock()
        usecase = ShortenUrlUsecase(repo)
        handler = ShortenUrlHandler(usecase)

        body = {
            "original_url": ''
        }

        with pytest.raises(HTTPException):
            handler(body)