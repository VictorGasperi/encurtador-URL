import pytest
from app.modules.url_management.application.shorten_url_usecase import ShortenUrlUsecase
from app.modules.url_management.domain.exceptions import InvalidUrlException
from app.modules.url_management.infrastructure.repositories.url_repository_mock import UrlRepositoryMock

class TestShortenUrlUsecase():

    def test_shorten_url_usecase(self):
        repo = UrlRepositoryMock()
        usecase = ShortenUrlUsecase(repo)

        response = usecase('test.shorten')
        assert response.original_url == 'test.shorten'
        assert len(response.code) == 6
        assert response.ttl == None

    def test_shorten_url_usecase_with_ttl(self):
        repo = UrlRepositoryMock()
        usecase = ShortenUrlUsecase(repo)

        response = usecase('exemplo.com', 3600)
        assert response.original_url == 'exemplo.com'
        assert response.ttl != None
    
    def test_shorten_url_usecase_invalid_url(self):
        repo = UrlRepositoryMock()
        usecase = ShortenUrlUsecase(repo)

        with pytest.raises(InvalidUrlException):
            usecase(original_url='')