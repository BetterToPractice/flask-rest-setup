from flask import Blueprint, Flask

from project.extensions import pluggy

from .views import home_view

impl = pluggy.get_impl()


@impl
def load_routes(app: Flask):
    bp = Blueprint("core", __name__)
    bp.add_url_rule("/", view_func=home_view, methods=["GET"])

    app.register_blueprint(blueprint=bp)
