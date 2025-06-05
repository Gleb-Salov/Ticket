from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from .db_session import get_session
from auth_service.domain import User
from auth_service.services import jwt_validator
from uuid import UUID
from typing import cast

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> User:
    try:
        payload = jwt_validator.decode_jwt(token)
        user_id_raw = payload.get("sub")
        if user_id_raw is None:
            raise ValueError("Missing subject in token")

        try:
            user_id = UUID(user_id_raw)
        except ValueError:
            raise ValueError("Subject must be a valid UUID")

    except (JWTError, ValueError) as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return cast(User, user)
