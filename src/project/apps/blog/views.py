from apifairy import arguments, response

from .models import Post
from .schemas import post_pagination_schema, post_params_schema, post_schema
from .services import post_service


@arguments(post_params_schema)
@response(post_pagination_schema)
def post_list_view(params):
    result = post_service.query(params)
    return result


@response(post_schema)
def post_detail_view(post_id):
    user = Post.query.filter_by(id=post_id).first_or_404()
    return user
