from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    title : str = "the conduct application"
    version : float = 1.0
    programmer : str = "Shahriyar Tarnasi"
    programmer_email : str = "shahryar.tarnasi@gmail.com"
    framework : str = "fastapi"
    
    model_config = SettingsConfigDict(env_file="../.env")


setting = Settings()
