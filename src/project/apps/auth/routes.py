from flask import Blueprint, Flask

from project.extensions import pluggy

from .views import activate_account_view, login_view, register_view

impl = pluggy.get_impl()


@impl
def load_routes(app: Flask):
    bp = Blueprint("auth", __name__)

    bp.add_url_rule("/login/", view_func=login_view, methods=["POST"])
    bp.add_url_rule("/register/", view_func=register_view, methods=["POST"])
    bp.add_url_rule("/activate-account/", view_func=activate_account_view, methods=["POST"])

    app.register_blueprint(blueprint=bp)
