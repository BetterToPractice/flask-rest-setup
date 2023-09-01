from marshmallow import fields

from project.apps.core.schemas import PaginationSchema
from project.extensions import ma


class UserSchema(ma.Schema):
    id = ma.Integer()
    username = ma.String()
    name = ma.String()
    email = ma.String()


class UserPaginationSchema(ma.Schema):
    data = fields.Nested(UserSchema(many=True))
    pagination = fields.Nested(PaginationSchema())


user_pagination_schema = UserPaginationSchema()
user_schema = UserSchema()
