from functools import lru_cache
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    app_name: str = "Mock Razorpay Payment API"
    env: str = "local"

    mongo_uri: str = "mongodb://localhost:27017"
    mongo_db_name: str = "mock_payment_api"

    # For a real Razorpay integration you would keep keys here (env vars only)
    razorpay_key_id: str | None = None
    razorpay_key_secret: str | None = None

    backend_cors_origins: list[AnyHttpUrl] | list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()


