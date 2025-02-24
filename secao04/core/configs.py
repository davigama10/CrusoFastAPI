from typing import List

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):

    #Configurações gerais usadas na aplicação

    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:84265@localhost:5432/faculdade"
    DBBaseModel: type = declarative_base()

    class Config:
        case_sensitive = True



settings = Settings()