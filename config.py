import os

basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SECRET_KEY = os.environ.get("SECRET_KEY")

    CACHE_TYPE = os.environ.get("CACHE_TYPE")
    CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL') or 'redis://localhost:6379/0'
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get("CACHE_DEFAULT_TIMEOUT"))
