from fastapi import APIRouter


router = APIRouter()

url_repository = Environments.get_url_repository()()