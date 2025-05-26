from fastapi import FastAPI
from auth_service.app import auth_routers, user_routers
from auth_service.db import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth_routers)
app.include_router(user_routers)

