from enum import Enum
from os import environ, urandom
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


class ConfigType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"


class Config:
    SECRET_KEY = environ.get("SECRET_KEY") or urandom(32).hex()

    # MongoDB
    MONGO_DB_NAME = environ.get("MONGO_DB_NAME") or "pyhoot-mongo-db"
    MONGO_DB_PROTOCOL = environ.get("MONGO_DB_PROTOCOL")
    MONGO_DB_USER = environ.get("MONGO_DB_USER")
    MONGO_DB_PASS = environ.get("MONGO_DB_PASS")
    MONGO_DB_HOST = environ.get("MONGO_DB_HOST")
    MONGO_DB_PORT = environ.get("MONGO_DB_PORT")

    # MySQL
    MYSQL_DB_NAME = environ.get("MYSQL_DB_NAME") or "pyhoot-mysql-db"
    MYSQL_DB_PROTOCOL = environ.get("MYSQL_DB_PROTOCOL")
    MYSQL_DB_USER = environ.get("MYSQL_DB_USER")
    MYSQL_DB_PASS = environ.get("MYSQL_DB_PASS")
    MYSQL_DB_HOST = environ.get("MYSQL_DB_HOST")
    MYSQL_DB_PORT = environ.get("MYSQL_DB_PORT")

    # Flask-Mail
    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = environ.get("MAIL_USE_TLS")
    MAIL_SENDER = environ.get("MAIL_SENDER")
    MAIL_PORT = environ.get("MAIL_PORT")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get(f"{Config.MYSQL_DB_NAME}_DEV") or f"sqlite:///{BASE_DIR}/data-dev.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get(Config.MYSQL_DB_NAME) or f"sqlite:///{BASE_DIR}/data-prod.sqlite"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get(f"{Config.MYSQL_DB_NAME}_TEST") or f"sqlite:///"


__configs = {
    ConfigType.DEVELOPMENT: DevelopmentConfig,
    ConfigType.PRODUCTION: ProductionConfig,
    ConfigType.TESTING: TestingConfig,
}


def configure(_app: Flask, config_type: ConfigType) -> None:
    _app.config.from_object(__configs[config_type])
    _app.config["MONGO_DB_URI"] = (f"{_app.config['MONGO_DB_PROTOCOL']}://{_app.config['MONGO_DB_USER']}:"
                                   f"{_app.config['MONGO_DB_PASS']}@{_app.config['MONGO_DB_HOST']}:"
                                   f"{_app.config['MONGO_DB_PORT']}")

    from .persistence.db import init_mongodb
    init_mongodb(_app.config["MONGO_DB_URI"], _app.config["MONGO_DB_NAME"])
