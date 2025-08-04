from fastapi import HTTPException
from app.modules.url_management.application.shorten_url_usecase import ShortenUrlUsecase
from app.modules.url_management.domain.exceptions import InvalidUrlException, UrlNotFoundException


class ShortenUrlHandler():

    def __init__(self, usecase: ShortenUrlUsecase):
        self.usecase = usecase

    def __call__(self, body: dict):
        try:
            response = self.usecase(body.get("original_url"))
            return {
                "original_url": response.original_url,
                "code": response.code
            }
        except InvalidUrlException as e:
            raise HTTPException(status_code=422, detail=str(e))
        except UrlNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail='Internal server error.')