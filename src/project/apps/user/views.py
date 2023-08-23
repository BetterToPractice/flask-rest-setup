from apifairy import response
from sqlalchemy import select

from project.extensions import db

from .models import User
from .schemas import users_schema


@response(users_schema)
def user_list_view():
    users = db.session.execute(select(User).order_by(User.username)).scalars()
    return users
