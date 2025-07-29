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
    print('A MAGIA DO PRINT. AQUI ESTÁ A REQUEST:  ')
    print(request)
    return {"message": "Lambda container funcionando!"}

handler = Mangum(app, lifespan="off", api_gateway_base_path='/test')
