from pydantic import BaseSettings

class Settings(BaseSettings):

    secret_key: str
    sage_key: str
    sage_url: str = 'https://www.promoplace.com/ws/ws.dll/ConnectAPI'
    sage_acct: int
    debugging: bool = True

    class Config:
        env_file = ".env"


settings = Settings()