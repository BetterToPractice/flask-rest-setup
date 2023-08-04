from apifairy import APIFairy
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app_fairy = APIFairy()
migrate = Migrate(compare_type=True)
db = SQLAlchemy()
