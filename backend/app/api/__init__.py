from fastapi import APIRouter
from app.api.routes_auth import router as auth_router
#from app.api.routes_jobs import router as jobs_router
#rom app.api.routes_users import router as users_router

router = APIRouter()

router.include_router(auth_router, prefix = "/routes_auth")
#router.include_router(jobs_router)
#router.include_router(users_router)
