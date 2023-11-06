from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_URI: str
    PORT: int

    class Config:
        env_file = ".env"


settings = Settings()
