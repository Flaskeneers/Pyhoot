from app import create_app
from app.config import ConfigType

app = create_app(config_type=ConfigType.DEVELOPMENT)

if __name__ == "__main__":
    app.run()
