import os

basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SECRET_KEY = os.environ.get("SECRET_KEY")
