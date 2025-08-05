import json
from fastapi import APIRouter, Request

from app.modules.url_management.application.shorten_url_usecase import ShortenUrlUsecase
from app.modules.url_management.presentation.handlers.shorten_url_handler import ShortenUrlHandler
from app.shared.environments import Environments

router = APIRouter()

url_repository = Environments.get_url_repository()()
shorten_url_usecase = ShortenUrlUsecase(url_repository)
shorten_url_handler = ShortenUrlHandler(shorten_url_usecase)

@router.post("/shorten")
async def shorten_url(request: Request):
    raw_body = await request.body()
    body = json.loads(raw_body.decode())
    response = shorten_url_handler(body)
    return response
