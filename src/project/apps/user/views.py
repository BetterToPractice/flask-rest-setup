from apifairy import response

from .models import User
from .schemas import user_schema, users_schema


@response(users_schema)
def user_list_view():
    users = User.query.all()
    return users


@response(user_schema)
def user_detail_view(username):
    user = User.query.filter_by(username=username).first_or_404()
    return user
