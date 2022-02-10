from os import getenv

from app import create_app
from app.config import ConfigType
from app import socketio

from dotenv import load_dotenv

load_dotenv()

ENV = getenv("PROJECT_ENV")
application = create_app(config_type=ConfigType(ENV.lower()))

if __name__ == "__main__":
    socketio.run(application, debug=True)
