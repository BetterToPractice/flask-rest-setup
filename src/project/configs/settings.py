from pathlib import Path

APP_NAME = "project"


class Settings:
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    APP_DIR = Path(__file__).parent

    # API Fairy
    # https://apifairy.readthedocs.io/en/latest/intro.html
    APIFAIRY_UI_PATH = "/"
