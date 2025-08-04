from fastapi import FastAPI
from mangum import Mangum

from app.modules.url_management.presentation import url_router
from app.shared.environments import Environments

stage = Environments.get_envs().stage

base_path = '/' + stage
app = FastAPI(root_path=base_path)

@app.get('', include_in_schema=False)
async def fastapi_lambda_workaround(): return {}

app.include_router(url_router, prefix='/url')


handler = Mangum(app, lifespan="off", api_gateway_base_path=base_path)
