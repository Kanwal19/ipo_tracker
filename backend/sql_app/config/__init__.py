from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "IPO Tracker"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str = ""


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()