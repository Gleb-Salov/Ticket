import os
from jose import jwt, JWTError
from auth_service.infra import settings

class JWTValidator:
    def __init__(self, public_key_path: str = settings.JWT_PUBLIC_KEY_PATH, algorithm: str = "RS256"):
        self.algorithm = algorithm

        if not os.path.exists(public_key_path):
            raise FileNotFoundError(f"Public key file not found: {public_key_path}")
        with open(public_key_path, "r", encoding="utf-8") as f:
            self._public_key = f.read()

    def decode_jwt(self, token: str) -> dict:
        try:
            return jwt.decode(token, self._public_key, algorithms=[self.algorithm])
        except JWTError as e:
            raise JWTError(f"Invalid token: {str(e)}")

jwt_validator = JWTValidator()