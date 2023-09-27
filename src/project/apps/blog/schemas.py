from marshmallow import fields, validate

from project.apps.blog.models import Comment
from project.apps.core.schemas import PaginationSchema
from project.extensions import ma


class CommentSchema(ma.SQLAlchemySchema):
    body = ma.String()

    class Meta:
        model = Comment


class PostParamsSchema(ma.Schema):
    q = ma.String()
    page = ma.Integer(missing=1)
    size = ma.Integer(missing=20, validate=validate.Range(min=1, max=50, error="Invalid"))


class PostSchema(ma.Schema):
    id = ma.Integer()
    title = ma.String()
    body = ma.String()
    comments = ma.Nested(CommentSchema, attribute="comments", many=True)


class PostPaginationSchema(ma.Schema):
    data = fields.Nested(PostSchema(many=True))
    pagination = fields.Nested(PaginationSchema())


post_pagination_schema = PostPaginationSchema()
post_params_schema = PostParamsSchema()
post_schema = PostSchema()
