from fastapi import FastAPI, Request
from mangum import Mangum
import os
from dotenv import load_dotenv

load_dotenv()

base_path = '/' + os.environ.get('stage')
app = FastAPI(root_path=base_path)

@app.get('', include_in_schema=False)
async def fastapi_lambda_workaround(): return {}


app.include_router(url_router, prefix='/url')


handler = Mangum(app, lifespan="off", api_gateway_base_path=base_path)
