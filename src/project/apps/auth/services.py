from flask_jwt_extended import create_access_token, create_refresh_token

from project.apps.auth.mails import register_mail
from project.apps.auth.tokens import ActivateAccountTokenGenerator
from project.apps.user.models import User, UserProfile
from project.extensions import db


def register(register_data):
    user = User(**register_data)
    user.profile = UserProfile()
    user.set_password(register_data["password"])
    db.session.add(user)
    db.session.commit()

    register_mail.send(
        recipients=user.email,
        context={
            "name": user.name,
            "url": ActivateAccountTokenGenerator().generate_url(user),
        },
    )

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


def activate_account(token_data):
    is_valid, user = ActivateAccountTokenGenerator().validate(token_data["token"])
    if not is_valid:
        return False

    user.is_email_confirmed = True
    db.session.add(user)
    db.session.commit()

    return True
