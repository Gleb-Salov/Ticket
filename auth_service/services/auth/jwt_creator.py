import os
from datetime import datetime, timedelta
from jose import jwt
from auth_service.infra import settings

class JWTCreator:
    def __init__(self, private_key_path: str = settings.JWT_PRIVATE_KEY_PATH, algorithm: str = "RS256", expire_minutes: int = 60):
        self.algorithm = algorithm
        self.expire_minutes = expire_minutes

        if not os.path.exists(private_key_path):
            raise FileNotFoundError(f"Private key file not found: {private_key_path}")
        with open(private_key_path, "r", encoding="utf-8") as f:
            self._private_key = f.read()

    def create_jwt(self, user_id: str) -> str:
        headers = {"alg": self.algorithm, "typ": "JWT"}
        payload = {
            "sub": user_id,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=self.expire_minutes),
        }
        return jwt.encode(payload, self._private_key, algorithm=self.algorithm, headers=headers)

jwt_creat = JWTCreator()