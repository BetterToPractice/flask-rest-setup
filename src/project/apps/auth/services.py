from flask_jwt_extended import create_access_token, create_refresh_token

from project.apps.user.models import User, UserProfile
from project.extensions import db


def register(register_data):
    user = User(**register_data)
    user.profile = UserProfile()
    user.set_password(register_data["password"])
    db.session.add(user)
    db.session.commit()
    return user


def create_token(user):
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    return {
        "access": access_token,
        "refresh": refresh_token,
    }


def get_user(username, password=None):
    user = User.query.filter_by(username=username).first()
    if not user:
        return None
    if password and not user.check_password(password):
        return None
    return user
