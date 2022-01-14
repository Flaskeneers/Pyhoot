from flask import Flask
# from flask_login import LoginManager

# login_manager = LoginManager()


# non-initialized extensions


def create_app() -> Flask:
    app = Flask(__name__)

    # initialize from config file
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
