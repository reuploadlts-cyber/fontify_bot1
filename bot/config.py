import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    bot_token: str
    bot_username: str
    channel_username: str
    webhook_base_url: str
    webhook_secret: str
    app_host: str
    app_port: int
    app_name: str
    environment: str

    @property
    def webhook_path(self) -> str:
        return f"/webhook/{self.webhook_secret}"

    @property
    def webhook_url(self) -> str:
        return f"{self.webhook_base_url}{self.webhook_path}"


def _get_required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"{name} is missing in .env")
    return value


def get_settings() -> Settings:
    bot_token = _get_required_env("BOT_TOKEN")
    bot_username = _get_required_env("BOT_USERNAME")
    channel_username = _get_required_env("CHANNEL_USERNAME")
    webhook_base_url = _get_required_env("WEBHOOK_BASE_URL").rstrip("/")
    webhook_secret = _get_required_env("WEBHOOK_SECRET")
    app_host = os.getenv("APP_HOST", "0.0.0.0").strip() or "0.0.0.0"
    app_port_raw = os.getenv("APP_PORT", "10000").strip() or "10000"
    app_name = os.getenv("APP_NAME", "FontifyBot").strip() or "FontifyBot"
    environment = os.getenv("ENVIRONMENT", "production").strip().lower() or "production"

    if not channel_username.startswith("@"):
        raise ValueError("CHANNEL_USERNAME must start with '@'")

    try:
        app_port = int(app_port_raw)
    except ValueError as exc:
        raise ValueError("APP_PORT must be a valid integer") from exc

    return Settings(
        bot_token=bot_token,
        bot_username=bot_username,
        channel_username=channel_username,
        webhook_base_url=webhook_base_url,
        webhook_secret=webhook_secret,
        app_host=app_host,
        app_port=app_port,
        app_name=app_name,
        environment=environment,
    )


settings = get_settings()
