from apifairy import APIFairy
from flask_bcrypt import Bcrypt
from flask_compress import Compress
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from project.libs.helmet import FlaskHelmet
from project.libs.plugin import Plugin

api_fairy = APIFairy()
migrate = Migrate(compare_type=True)
db = SQLAlchemy()
pluggy = Plugin()
bcrypt = Bcrypt()
ma = Marshmallow()
compress = Compress()
cors = CORS()
helmet = FlaskHelmet()
