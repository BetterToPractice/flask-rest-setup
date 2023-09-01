from apifairy import response

from project.extensions import pagination

from .models import User
from .schemas import user_pagination_schema, user_schema


@response(user_pagination_schema)
def user_list_view():
    result = pagination.paginate(User.query.all(), user_schema, marshmallow=True)
    return result


@response(user_schema)
def user_detail_view(username):
    user = User.query.filter_by(username=username).first_or_404()
    return user
