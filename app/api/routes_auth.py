#login, logout, register, etc
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'message' : 'yo yo testing'}