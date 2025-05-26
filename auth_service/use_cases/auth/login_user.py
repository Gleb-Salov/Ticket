from sqlalchemy.orm import Session
from auth_service.infra import get_session
from auth_service.domain import User
from auth_service.services import verify_password, jwt_creat
from fastapi import HTTPException, Depends
from typing import Optional

class AuthService:
    def __init__(self, session: Session):
        self.session = session

    def login_user(self, username: str, password: str) -> str:
        user: Optional[User] = self.session.query(User).filter(User.name == username).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid user data")
        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid user data")

        return jwt_creat.create_jwt(str(user.id))

def get_auth_session(session: Session = Depends(get_session)) -> AuthService:
    return AuthService(session = session)