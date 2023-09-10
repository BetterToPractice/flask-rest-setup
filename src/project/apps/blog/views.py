from apifairy import response

from project.extensions import pagination

from .models import Post
from .schemas import (
    post_pagination_schema,
    post_schema,
)


@response(post_pagination_schema)
def post_list_view():
    result = pagination.paginate(Post.query.all(), post_schema, marshmallow=True)
    return result


@response(post_schema)
def post_detail_view(post_id):
    user = Post.query.filter_by(id=post_id).first_or_404()
    return user
