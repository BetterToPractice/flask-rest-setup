from marshmallow import fields, validate

from project.apps.core.schemas import PaginationSchema
from project.apps.user.models import User, UserProfile
from project.extensions import ma


class ProfileSchema(ma.SQLAlchemySchema):
    gender = ma.String(validate=validate.OneOf(choices=[e.value for e in UserProfile.GenderEnum]))
    phone_number = ma.String()

    class Meta:
        model = UserProfile


class UserSchema(ma.SQLAlchemySchema):
    id = ma.Integer()
    username = ma.String()
    name = ma.String()
    email = ma.String()
    profile = ma.Nested(ProfileSchema, attribute="profile", many=False)

    class Meta:
        model = User


class UserPaginationSchema(ma.Schema):
    data = fields.Nested(UserSchema(many=True))
    pagination = fields.Nested(PaginationSchema())


user_pagination_schema = UserPaginationSchema()
user_schema = UserSchema()
