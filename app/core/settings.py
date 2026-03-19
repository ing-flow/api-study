from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    database_url: str
    log_level: str = "INFO"

    # 追加
    env: str = "local" # local / dev / prod

    class Config:
        env_file = ".env"


settings = Settings()