from datetime import datetime, timedelta

from flask import current_app
from itsdangerous import BadTimeSignature
from itsdangerous import URLSafeTimedSerializer as Serializer

from project.apps.user.models import User


class TokenGenerator:
    TOKEN_EXPIRES = None
    TOKEN_SALT = None

    def __init__(self):
        self.serializer = Serializer(current_app.config.get("SECRET_KEY") or "foobar")

    def generate(self, *_, **kwargs):
        expires_in = (datetime.utcnow() + timedelta(seconds=self.TOKEN_EXPIRES)).strftime("%Y-%m-%d %H:%M:%S")
        token = self.serializer.dumps({**kwargs, "__exp": expires_in}, salt=self.TOKEN_SALT)
        return token

    def validate(self, token):
        try:
            data = self.serializer.loads(token, salt=self.TOKEN_SALT)
        except BadTimeSignature:
            return False, None

        expires_in = datetime.strptime(data.pop("__exp"), "%Y-%m-%d %H:%M:%S")
        if expires_in < datetime.utcnow():
            return False, None
        return True, data


class UserTokenGenerator(TokenGenerator):
    identifier_db = "username"
    identifier = "__user_username"

    TOKEN_SALT = "user-auth"
    TOKEN_EXPIRES = 12 * 60 * 60  # one day

    def generate(self, user):
        return super().generate(**self.get_data(user))

    def generate_url(self, user):
        raise NotImplementedError("not yet implemented")

    def validate(self, token):
        is_valid, data = super().validate(token=token)
        if not is_valid or self.identifier not in data:
            return False, None

        user = User.query.filter_by(**{self.identifier_db: data[self.identifier]}).first()
        if user is None:
            return False, None

        user_data = self.get_data(user)
        for d in data.keys():
            if d not in user_data or str(user_data[d]) != str(data[d]):
                return False, None

        return True, user

    def get_data(self, user):
        return {
            self.identifier: user.username,
        }
