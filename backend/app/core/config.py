import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "AI Agent")
    DEBUG = os.getenv("DEBUG", "False") == "True"

    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")


settings = Settings()
