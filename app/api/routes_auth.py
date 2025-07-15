#login, logout, register, etc
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'message' : 'yo yo testing'}

@app.get("/login")
async def get_login():
    pass
@app.post("login")
async def post_login():
    pass
@app.get("/homepage")
async def home():
    pass