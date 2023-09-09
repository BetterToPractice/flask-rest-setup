from marshmallow import EXCLUDE, ValidationError, validate, validates, validates_schema

from project.apps.auth import services
from project.apps.user.models import User
from project.extensions import ma


class RegisterSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    name = ma.auto_field(
        required=True,
        validate=validate.Length(min=3, max=250),
    )
    username = ma.auto_field(
        required=True,
        validate=validate.Length(min=6, max=50),
    )
    email = ma.auto_field(
        required=True,
        validate=[validate.Length(max=250), validate.Email()],
    )
    password = ma.String(
        required=True,
        load_only=True,
        validate=validate.Length(min=6, max=50),
    )

    @validates("username")
    def validate_username(self, value):
        user = User.query.filter_by(username=value).first()
        if user:
            raise ValidationError("username already used")

    @validates("email")
    def validate_email(self, value):
        user = User.query.filter_by(email=value).first()
        if user:
            raise ValidationError("email already used")


class LoginSchema(ma.Schema):
    username = ma.String(
        required=True,
        validate=validate.Length(min=6, max=50),
    )
    password = ma.String(
        required=True,
        load_only=True,
        validate=validate.Length(min=6, max=50),
    )

    class Meta:
        unknown = EXCLUDE

    @validates_schema
    def validation_not_match(self, data, **kwargs):
        user = services.get_user(username=data["username"], password=data["password"])
        if not user:
            raise ValidationError("username or password not match", "username")


class TokenResponseSchema(ma.Schema):
    access = ma.String()
    refresh = ma.String()


register_schema = RegisterSchema()
login_schema = LoginSchema()
token_response_schema = TokenResponseSchema()
