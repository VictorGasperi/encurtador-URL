from fastapi import FastAPI
from mangum import Mangum

from app.modules.url_management.presentation.url_router import router
from app.shared.environments import Environments

root = Environments.get_envs().stage.value

base_path = '/' + root
app = FastAPI(root_path=base_path)

@app.get('', include_in_schema=False)
@app.get('/health')
async def health():
    return {
        "message": "API Running!",
        "base_path": base_path    
    }

app.include_router(router, prefix='/url')

handler = Mangum(app, lifespan="off", api_gateway_base_path=base_path)
