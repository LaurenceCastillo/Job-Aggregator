from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
 
from app.api import router as api_router

#from app.api.routes import router as api_router
from app.api import routes_auth
from app.api import routes_jobs
from app.api import routes_users
 
def get_application():
    app = FastAPI(title="Phresh", version="1.0.0")
 
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
 
    app.include_router(api_router, prefix="/api")
    #app.include_router(routes_auth, prefix = "/api")
    #app.include_router(routes_jobs, prefix = "/api")
    #app.include_router(routes_users, prefix = "/api")

    return app
 
 
app = get_application()