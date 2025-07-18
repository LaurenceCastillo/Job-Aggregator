#login, logout, register, etc
from fastapi import FastAPI
from fastapi import APIRouter
from typing import List

router = APIRouter()




@router.get("/")
async def get_all_cleanings() -> List[dict]:
    cleanings = [
        {"id": 1, "name": "My house", "cleaning_type": "full_clean", "price_per_hour": 29.99},
        {"id": 2, "name": "Someone else's house", "cleaning_type": "spot_clean", "price_per_hour": 19.99}
    ]
 
    return cleanings
#@app.get("/")
#async def root():
#    return {'message' : 'yo yo testing'}

@router.get("/login")
async def get_login():
    pass
@router.post("login")
async def post_login():
    pass
@router.get("/homepage")
async def home():
    pass