from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LEVEL: str
    PROJECT_TITLE: str = 'Movie Quiz API'
    COMMON_API: str
    
    class Config:
        env_file = '.env'
        

class DevelopSettings(Settings):
    DB_URL: str = Field(env='DEVELOP_DB_URL')
    

class ProductSettings(Settings):
    DB_URL: str = Field(env='PRODUCT_DB_URL')
    
    
@lru_cache
def get_settings():
    return DevelopSettings() if Settings().LEVEL == 'DEVELOP' \
        else ProductSettings()