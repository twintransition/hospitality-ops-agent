from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Hospitality Operations Agent"
    api_prefix: str = ""
    frontend_origin: str = "http://localhost:3000"


settings = Settings()
