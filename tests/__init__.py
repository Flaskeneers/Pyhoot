import unittest

from app import create_app
from app.config import ConfigType
from app.persistence import db as pymongo


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = create_app(ConfigType.TESTING)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls) -> None:
        pymongo.drop_database(cls.app.config["MONGO_DB_NAME"])
        cls.app_context.pop()


if __name__ == "__main__":
    unittest.main()
