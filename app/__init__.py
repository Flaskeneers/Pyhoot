from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_mail import Mail

from . import errors
from app.config import ConfigType, configure

login_manager = LoginManager()
socketio = SocketIO()
mail = Mail()


def create_app(config_type: ConfigType = ConfigType.DEVELOPMENT) -> Flask:
    _app = Flask(__name__)

    configure(_app, config_type)
    initialize_extensions(_app)
    register_blueprints(_app)

    errors.register_error_handlers(_app)

    mail.init_app(_app)

    return _app


def initialize_extensions(_app: Flask) -> None:
    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.persistence.models.user import User
        return User.find(username=user_id).first_or_none()

    socketio.init_app(_app)


def register_blueprints(_app: Flask) -> None:
    from app.blueprints.auth import bp_auth
    _app.register_blueprint(bp_auth)

    from app.blueprints.api import bp_api
    _app.register_blueprint(bp_api, url_prefix="/api/1.0")

    from app.blueprints.guest import bp_guest
    _app.register_blueprint(bp_guest)

    from app.blueprints.game import bp_game
    _app.register_blueprint(bp_game, url_prefix="/game")

    from app.blueprints.user import bp_user
    _app.register_blueprint(bp_user)

