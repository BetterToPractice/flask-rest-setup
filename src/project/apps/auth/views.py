from apifairy import body, response

from project.apps.auth.schemas import (
    login_schema,
    register_schema,
    token_response_schema,
)
from project.apps.user.models import User
from project.extensions import jwt

from . import services


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@body(login_schema)
@response(token_response_schema)
def login_view(args):
    user = services.get_user(
        username=args["username"],
        password=args["password"],
    )
    return services.create_token(user)


@body(register_schema)
@response(token_response_schema)
def register_view(register_data):
    user = services.register(register_data=register_data)
    token = services.create_token(user)
    return token
