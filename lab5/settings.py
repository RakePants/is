from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: int = 5432
    database_password: str
    database_name: str
    database_username: str

    class Config:
        extra = 'ignore'
        env_file = '.env'  # Specify the location of your .env file here


settings = Settings()
