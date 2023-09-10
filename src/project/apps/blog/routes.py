from flask import Blueprint, Flask

from project.extensions import pluggy

from .views import (
    post_detail_view,
    post_list_view,
)

impl = pluggy.get_impl()


@impl
def load_routes(app: Flask):
    bp = Blueprint("blog", __name__)

    bp.add_url_rule("/posts/", view_func=post_list_view, methods=["GET"])
    bp.add_url_rule("/posts/<int:post_id>/", view_func=post_detail_view, methods=["GET"])

    app.register_blueprint(blueprint=bp)
