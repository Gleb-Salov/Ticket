from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_HOST: str

    JWT_PRIVATE_KEY_PATH: str
    JWT_PUBLIC_KEY_PATH: str

    @property
    def database_url(self) -> str:
        return(
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    class Config:
        env_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()



