from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Lambda container funcionando!"}

handler = Mangum(app)
