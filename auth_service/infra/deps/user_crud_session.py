from fastapi import Depends
from sqlalchemy.orm import Session
from .db_session import get_session
from auth_service.infra.db.repositories.user_crud import UserCRUD

def get_user_crud(session: Session = Depends(get_session)) -> UserCRUD:
    return UserCRUD(session)