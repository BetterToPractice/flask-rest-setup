from flask import Flask

from . import commands
from .settings import Settings


def create_app():
    app = Flask(__name__.split(".")[0])
    load_setting(app)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def load_setting(app):
    app.config.from_object(Settings)


def register_blueprints(app):
    app.extensions["plugin"].hook.load_routes(app=app)


def register_extensions(app):
    from project.configs import plugins
    from project.extensions import (
        api_fairy,
        bcrypt,
        compress,
        cors,
        db,
        helmet,
        jwt,
        ma,
        mail,
        migrate,
        pagination,
        pluggy,
    )

    cors.init_app(app)
    compress.init_app(app)
    helmet.init_app(app)
    ma.init_app(app)
    api_fairy.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db=db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    pagination.init_app(app)
    pluggy.init_app(
        app, plugin_name="plugins", hook_specs=plugins, apps_paths="apps", ignore_imports_prefix=[".models"]
    )


def register_commands(app):
    app.cli.add_command(commands.foo)
