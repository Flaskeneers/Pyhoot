from app import create_app
from app.config import ConfigType
from app import socketio

application = create_app(config_type=ConfigType.DEVELOPMENT)

if __name__ == "__main__":
    socketio.run(application, debug=True)
