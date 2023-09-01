from flask import Blueprint, Flask

from project.extensions import pluggy

from .views import (
    category_detail_view,
    category_list_view,
    post_detail_view,
    post_list_view,
)

impl = pluggy.get_impl()


@impl
def load_routes(app: Flask):
    bp = Blueprint("blog", __name__)

    bp.add_url_rule("/categories/", view_func=category_list_view, methods=["GET"])
    bp.add_url_rule("/categories/<int:category_id>/", view_func=category_detail_view, methods=["GET"])
    bp.add_url_rule("/posts/", view_func=post_list_view, methods=["GET"])
    bp.add_url_rule("/posts/<int:post_id>/", view_func=post_detail_view, methods=["GET"])

    app.register_blueprint(blueprint=bp)
