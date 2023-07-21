from pydantic import BaseSettings
from decouple import config


class Settings(BaseSettings):
    API_STR: str "/api"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    
