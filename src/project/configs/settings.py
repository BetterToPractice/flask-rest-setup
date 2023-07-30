import os
from pathlib import Path
from dotenv import load_dotenv

# Path
ROOT_DIR = Path(__file__).parent.parent.parent
APP_DIR = Path(__file__).parent


# Python Dotenv
# https://github.com/theskumar/python-dotenv
load_dotenv(dotenv_path=ROOT_DIR)


class Settings:
    APP_NAME = "project"
    FLASK_DEBUG = os.environ.get("DEBUG", default=False)
    FLASK_ENV = os.environ.get("FLASK_ENV", default="development")

    # API Fairy
    # https://apifairy.readthedocs.io/en/latest/intro.html
    APIFAIRY_UI_PATH = "/"
