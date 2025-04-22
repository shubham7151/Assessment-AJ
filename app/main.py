from fastapi import FastAPI
from app.api.v1.endpoints import extractdata

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "AJ-Bell"}

app.include_router(extractdata.router, prefix="/api/v1")