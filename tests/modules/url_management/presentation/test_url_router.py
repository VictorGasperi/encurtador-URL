from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestUrlRouter:

    def setup_method(self):
        from app.modules.url_management.presentation.url_router import url_router
        self.app = FastAPI()
        self.app.include_router(url_router, prefix='/url')
        self.client = TestClient(self.app)

    def test_shorten_route(self):
        response = self.client.post(
            "/url/shorten",
            json = {
                "original_url": "exeplo_de_url"
            }
        )

        assert response.status_code == 200
        data = response.json()
        assert len(data.get('code')) == 6

    def test_shorten_route_invalid_url(self):
        response = self.client.post(
            "/url/shorten",
            json = {
                "original_url": ""
            }
        )
        assert response.status_code == 422

        body = response.json()

        assert body['detail'] == f'The given URL \'\'\'\' is not valid.'
