from fastapi import FastAPI, Request
from mangum import Mangum
import os
from dotenv import load_dotenv

app = FastAPI(
    root_path='/test'
)

@app.get('', include_in_schema=False)
@app.get("/")
async def root(request: Request):
    return {"message": "COLOQUEI ALGO DIFERENTE"}

handler = Mangum(app, lifespan="off", api_gateway_base_path='/test')
