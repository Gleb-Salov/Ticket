from fastapi import Depends
from auth_service.schemas import UserCreate
from auth_service.services import hash_password

def hash_user_password(user: UserCreate = Depends()) -> UserCreate:
    hashed_user = user.copy(update={"password": hash_password(user.password)})
    return hashed_user