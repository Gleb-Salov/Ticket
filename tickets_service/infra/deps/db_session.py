from tickets_service.infra.db import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()