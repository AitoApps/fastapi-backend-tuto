from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_URI: str
    SECRET_KEY: str
    JWT_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
