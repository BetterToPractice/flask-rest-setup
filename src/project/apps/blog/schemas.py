from marshmallow import fields

from project.apps.core.schemas import PaginationSchema
from project.extensions import ma


class CategorySchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()


class CategoryPaginationSchema(ma.Schema):
    data = fields.Nested(CategorySchema(many=True))
    pagination = fields.Nested(PaginationSchema())


class PostSchema(ma.Schema):
    id = ma.Integer()
    title = ma.String()
    body = ma.String()


class PostPaginationSchema(ma.Schema):
    data = fields.Nested(PostSchema(many=True))
    pagination = fields.Nested(PaginationSchema())


category_pagination_schema = CategoryPaginationSchema()
category_schema = CategorySchema()

post_pagination_schema = PostPaginationSchema()
post_schema = PostSchema()
