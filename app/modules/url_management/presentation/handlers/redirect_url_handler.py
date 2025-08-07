from fastapi import HTTPException
from app.modules.url_management.application.redirect_url_usecase import RedirectUrlUsecase
from app.modules.url_management.domain.exceptions import InvalidCodeException, UrlNotFoundException


class RedirectUrlHandler():

    def __init__(self, usecase: RedirectUrlUsecase):
        self.usecase = usecase

    def __call__(self, code: str) -> str:

        try:
            
            response = self.usecase(code)
            return response
        
        except InvalidCodeException as e:
            raise HTTPException(status_code=422, detail=str(e))
        except UrlNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail='Internal server error.')