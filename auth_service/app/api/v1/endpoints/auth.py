from fastapi import APIRouter, Depends, Form
from auth_service.schemas import Token
from auth_service.use_cases import AuthService, get_auth_session

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=Token)
def login_oauth(
    username: str = Form(...),
    password: str = Form(...),
    crud: AuthService = Depends(get_auth_session),
) -> Token:
    token = crud.login_user(username, password)
    return Token(access_token=token, token_type="Bearer")