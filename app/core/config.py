from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postcode: str

    class Config:
        env_file = ".env"

settings = Settings()
