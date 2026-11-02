from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # adjust the number to land on your project root

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Jigsaw Puzzle API"
    cors_origins: list[str] = ["http://localhost:5173"]

    data_dir: Path = BASE_DIR / "data"
    image_path: Path = BASE_DIR / "data" / "sample.jpg"
    pieces_dir: Path = BASE_DIR / "data" / "pieces"

    max_grid_size: int = 20

@lru_cache
def get_settings() -> Settings:
    return Settings()
