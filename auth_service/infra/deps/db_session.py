from typing import Generator
from sqlalchemy.orm import Session
from auth_service.db.session import SessionLocal

def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()