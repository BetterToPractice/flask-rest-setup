from flask import Blueprint, Flask

from project.extensions import pluggy

from .views import user_list_view

impl = pluggy.get_impl()


@impl
def load_routes(app: Flask):
    bp = Blueprint("user", __name__)
    bp.add_url_rule("/users", view_func=user_list_view, methods=["GET"])

    app.register_blueprint(blueprint=bp)
