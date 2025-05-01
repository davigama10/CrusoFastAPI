from typing import List

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:84265@localhost:5432/faculdade"
    DBBaseModel: type = declarative_base()

    JWT_SECRET: str = 'POL5qNXBy3KpGR9_qLKEKLZ6wgyQJ5y6KP8TI1Vpxa8'
    """
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITH: str = 'HS256'
    # 60 minutos vezes 24 horas x 7 dias = 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7

    class Config:
        case_sentitive = True

settings: Settings = Settings()