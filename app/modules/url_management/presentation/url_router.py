import json
from fastapi import APIRouter, Request

from app.modules.url_management.application.shorten_url_usecase import ShortenUrlUsecase
from app.modules.url_management.presentation.handlers.shorten_url_handler import ShortenUrlHandler
from app.shared.environments import Environments

url_router = APIRouter()

url_repository = Environments.get_url_repository()()
shorten_url_usecase = ShortenUrlUsecase(url_repository)
shorten_url_controller = ShortenUrlHandler(shorten_url_usecase)

@url_router.post("/shorten")
async def shorten_url(request: Request):
    print('A MAGIA DO PRINT!!!!!!')
    print(Environments.get_envs().stage)
    print(Environments.get_envs().dynamo_table_name)
    raw_body = await request.body()
    body = json.loads(raw_body.decode())
    response = shorten_url_controller(body)
    return response
