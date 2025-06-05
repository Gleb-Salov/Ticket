import os
from jose import jwt, JWTError
from auth_service.infra import settings
from typing import Optional

class JWTValidator:
    def __init__(self, public_key_path: Optional[str] = settings.JWT_PUBLIC_KEY_PATH, algorithm: str = "RS256"):
        self.algorithm = algorithm

        public_key_path = public_key_path or settings.JWT_PUBLIC_KEY_PATH
        if public_key_path is None:
            raise ValueError("JWT_PUBLIC_KEY_PATH is not set in environment or passed explicitly")

        if not os.path.exists(public_key_path):
            raise FileNotFoundError(f"Public key file not found: {public_key_path}")
        with open(public_key_path, "r", encoding="utf-8") as key_file:
            self._public_key = key_file.read()

    def decode_jwt(self, token: str) -> dict:
        try:
            return jwt.decode(token, self._public_key, algorithms=[self.algorithm])
        except JWTError as e:
            raise JWTError(f"Invalid token: {str(e)}")

jwt_validator = JWTValidator()