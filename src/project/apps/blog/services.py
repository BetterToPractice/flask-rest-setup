from project.extensions import db, pagination

from .models import Post
from .schemas import post_schema


class PostService:
    @classmethod
    def query(cls, params):
        qs = db.session.query(Post)

        if params.get("q"):
            qs = qs.filter(Post.title.ilike(f'%{params["q"]}%'))

        return pagination.paginate(qs.all(), post_schema, marshmallow=True)


post_service = PostService()
