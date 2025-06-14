from fastapi import APIRouter, Depends, Form
from auth_service.schemas import Token
from auth_service.use_cases import AuthService, get_auth_session

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=Token)
def login_auth(
    username: str = Form(...),
    password: str = Form(...),
    auth: AuthService = Depends(get_auth_session),
) -> Token:
    token = auth.login_user(username, password)
    return Token(access_token=token, token_type="Bearer")