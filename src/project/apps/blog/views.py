from apifairy import response

from project.extensions import pagination

from .models import Category, Post
from .schemas import (
    category_pagination_schema,
    category_schema,
    post_pagination_schema,
    post_schema,
)


@response(category_pagination_schema)
def category_list_view():
    result = pagination.paginate(Category.query.all(), category_schema, marshmallow=True)
    return result


@response(category_schema)
def category_detail_view(category_id):
    user = Category.query.filter_by(id=category_id).first_or_404()
    return user


@response(post_pagination_schema)
def post_list_view():
    result = pagination.paginate(Post.query.all(), post_schema, marshmallow=True)
    return result


@response(post_schema)
def post_detail_view(post_id):
    user = Post.query.filter_by(id=post_id).first_or_404()
    return user
