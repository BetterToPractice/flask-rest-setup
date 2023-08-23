from apifairy import APIFairy
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from project.libs.plugin import Plugin


app_fairy = APIFairy()
migrate = Migrate(compare_type=True)
db = SQLAlchemy()
pluggy = Plugin()
