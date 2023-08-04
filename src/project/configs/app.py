from flask import Flask

from . import commands
from .settings import Settings


def create_app(setting=Settings):
    app = Flask(__name__.split(".")[0])

    load_setting(app, setting=setting)

    register_blueprints(app)
    register_commands(app)
    register_extensions(app)

    return app


def load_setting(app, setting):
    app.config.from_object(setting)


def register_blueprints(app):
    from project.apps.core import core as core_blueprint

    app.register_blueprint(core_blueprint)


def register_extensions(app):
    from .extensions import app_fairy

    app_fairy.init_app(app)


def register_commands(app):
    app.cli.add_command(commands.foo)
