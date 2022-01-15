from flask import Flask
# from flask_login import LoginManager

from .config import ConfigType, load_config


# TODO: non-initialized extensions
# login_manager = LoginManager()


def create_app(config_type: ConfigType = ConfigType.DEVELOPMENT) -> Flask:
    app = Flask(__name__)

    load_config(app, config_type)
    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app: Flask) -> None:
    from app.persistence.db import db
    db.init_app(app)

    # login_manager.init_app(app)


def register_blueprints(app: Flask) -> None:
    from app.blueprints.auth import bp_auth
    app.register_blueprint(bp_auth)

    from app.blueprints.guest import bp_guest
    app.register_blueprint(bp_guest)
