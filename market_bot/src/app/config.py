# Bot config file
import os
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: List[int]
    DB_URL: str = "sqlite+aiosqlite:///database/market_db.sqlite3"
    API_SITE: str
    TG_API_SITE: str
    FRONT_SITE: str
    TG_BOT_SITE: str
    API_PORT: str
    DB_ECHO: bool = True

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"),
        env_file_encoding="utf-8"
    )

    def get_webhook_url(self) -> str:
        """Возвращает URL вебхука."""
        return f"{self.API_SITE}/webhook"

    def get_tg_api_url(self) -> str:
        """Возвращает URL Telegram API."""
        return f"{self.TG_API_SITE}/bot{self.BOT_TOKEN}"


settings = Settings()
database_url = settings.DB_URL
