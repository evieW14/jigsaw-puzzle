from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Jigsaw Puzzle API"
    storage_backend: str = "json"
    data_dir: str = "/Users/eviewhite/coding/jigsaw-puzzle/data"
    cors_origins: list[str] = ["http://localhost:5173"]

@lru_cache
def get_settings() -> Settings:
    return Settings()
