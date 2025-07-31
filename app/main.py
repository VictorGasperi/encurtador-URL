from fastapi import FastAPI, Request
from mangum import Mangum
import os
from dotenv import load_dotenv

load_dotenv()

root = '/' + os.environ.get('stage')

app = FastAPI(
    root_path=root
)

@app.get('', include_in_schema=False)
@app.get("/")
async def root(request: Request):
    return {"message": "COLOQUEI ALGO DIFERENTE"}

handler = Mangum(app, lifespan="off", api_gateway_base_path=root)
