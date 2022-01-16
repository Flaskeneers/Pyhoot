from app import create_app
from app.config import ConfigType

application = create_app(config_type=ConfigType.DEVELOPMENT)

if __name__ == "__main__":
    application.run()
