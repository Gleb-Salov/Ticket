from fastapi import FastAPI
from tickets_service.app import tickets_router
from tickets_service.infra import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(tickets_router)


# uvicorn tickets_service.entrypoints.tickets_app:app
