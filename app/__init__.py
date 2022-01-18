from flask import Flask
# from flask_login import LoginManager

from app.config import ConfigType, configure


# TODO: non-initialized extensions
# login_manager = LoginManager()


def create_app(config_type: ConfigType = ConfigType.DEVELOPMENT) -> Flask:
    _app = Flask(__name__)

    configure(_app, config_type)
    initialize_extensions(_app)
    register_blueprints(_app)

    return _app


def initialize_extensions(_app: Flask) -> None:
    # login_manager.init_app(app)
    pass


def register_blueprints(_app: Flask) -> None:
    from app.blueprints.auth import bp_auth
    _app.register_blueprint(bp_auth)

    from app.blueprints.guest import bp_guest
    _app.register_blueprint(bp_guest)

    from app.blueprints.user import bp_user
    _app.register_blueprint(bp_user)
