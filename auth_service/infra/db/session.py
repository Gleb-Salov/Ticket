from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auth_service.infra import settings

DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)