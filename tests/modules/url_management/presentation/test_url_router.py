from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestUrlRouter:

    def setup_method(self):
        from app.modules.url_management.presentation.url_router import router
        self.app = FastAPI()
        self.app.include_router(router, prefix='/url')
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

    def test_shorten_route_with_ttl(self):
        response = self.client.post(
                    "/url/shorten",
                    json = {
                        "original_url": "exeplo_de_url",
                        "ttl": 3600
                    }
                )
        
        assert response.status_code == 200
        data = response.json()
        assert len(data.get('code')) == 6
        assert 'ttl' in data
        assert 'created_at' in data

    def test_shorten_route_invalid_url(self):
        response = self.client.post(
            "/url/shorten",
            json = {
                "original_url": ""
            }
        )
        assert response.status_code == 422

        body = response.json()

        assert body['detail'] == "The given URL '' is not valid."

    def test_redirect_route(self):
        response = self.client.get("/url/redirect/abcdef", allow_redirects=False)
        assert response.status_code == 307
        assert response.headers["location"] == "https://example.com/page2"

    def test_redirect_route_with_invalid_code(self):
        response = self.client.get("/url/redirect/123456789", allow_redirects=False)
        assert response.status_code == 422
        err_body = response.json()
        assert err_body['detail'] == "The given code '123456789' is not valid."

    def test_redirect_route_with_invalid_code(self):
        response = self.client.get("/url/redirect/fedcba", allow_redirects=False)
        assert response.status_code == 404
        err_body = response.json()
        assert err_body['detail'] == "URL with code 'fedcba' not found."