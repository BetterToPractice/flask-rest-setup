import os
from pathlib import Path

from dotenv import load_dotenv

# Path
ROOT_DIR = Path(__file__).parent.parent.parent


# Python Dotenv
# https://github.com/theskumar/python-dotenv
load_dotenv(dotenv_path=ROOT_DIR)


class Settings:
    APP_DIR = Path(__file__).parent.parent
    APP_NAME = "project"
    FLASK_DEBUG = os.environ.get("DEBUG", default=False)
    FLASK_ENV = os.environ.get("FLASK_ENV", default="development")

    # API Fairy
    # https://apifairy.readthedocs.io/en/latest/intro.html
    APIFAIRY_UI_PATH = "/docs"

    # SQLAlchemy
    # https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", default="sqlite:///db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_QUERY_TIMEOUT = 0.1
    SQLALCHEMY_RECORD_QUERIES = True

    # Cors
    # https://flask-cors.corydolphin.com/en/latest/api.html
    CORS_ALLOW_HEADERS = "*"
    CORS_ORIGINS = "*"
