from app.modules.url_management.domain.entities.short_url import ShortUrl
from app.modules.url_management.infrastructure.repositories.url_repository_mock import UrlRepositoryMock

class TestUrlRepositoryMock():

    def test_create_url(self):
        repo = UrlRepositoryMock()
        short_url = ShortUrl(code='asdq12', original_url='test_url')
        
        response = repo.create_url(short_url)

        assert short_url == repo.urls[3]
        assert response.code == short_url.code

    def test_get_url(self): 
        repo = UrlRepositoryMock()
        code = 'abcdef'
        response = repo.get_url(code)

        assert response.original_url == 'https://example.com/page2'

    def test_code_exists_true(self):
        repo = UrlRepositoryMock()
        response = repo.code_exists('qwerty')

        assert response == True

    def test_code_exists_false(self):
        repo = UrlRepositoryMock()
        response = repo.code_exists('vxaseq2')

        assert response == False