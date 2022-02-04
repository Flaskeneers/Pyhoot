import unittest

from app import create_app, ConfigType
from app.persistence import db as pymongo


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(ConfigType.TESTING)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        pymongo.drop_database(self.app.config["MONGO_DB_NAME"])
        self.app_context.pop()

    def test_does_db_names_match_from_env_var(self):
        self.assertEqual(self.app.config["MONGO_DB_NAME"], "pyhoot-mongo-db-test")


if __name__ == "__main__":
    unittest.main()
