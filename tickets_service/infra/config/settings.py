from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional
import os

class Settings(BaseSettings):
    POSTGRES_PORT: Optional[int] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_HOST: Optional[str] = None

    JWT_PUBLIC_KEY_PATH: Optional[str] = None
    JWT_PRIVATE_KEY_PATH: Optional[str] = None

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/tickets_db"
        )
    class Config:
        env_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..", ".env"))
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
