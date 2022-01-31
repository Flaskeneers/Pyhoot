import unittest

from tests import BaseTestCase


class UserTestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        # additional logic for testing user
        from app.controllers import user as user_controller
        cls.user_controller = user_controller

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        # additional logic

    def test_create_user(self):
        # create a user
        email = "jane.doe@example.com"
        username = "janedoe"
        password = "super-secret-password"
        self.user_controller.create_user(email, username, password)

        # verify user was created in database
        user = self.user_controller.get_by_username(username)
        self.assertIsNotNone(user)

        self.assertEqual(user.username, username)

        user = self.user_controller.get_by_username("emperor-fredrik")
        self.assertIsNone(user)

        # 1. create user
        #    - assert user does exist in db
        # 2. login user
        #    - check is logged in
        # 3. logout user
        #    - check user is not logged in
        # 4. delete account
        #    - assert user no longer exists in db

    def test_db(self):
        self.assertEqual(self.app.config["MONGO_DB_NAME"], "pyhoot-mongo-db-test")

        with self.app.app_context():
            self.assertEqual(self.app.config["MONGO_DB_NAME"], "pyhoot-mongo-db-test")


if __name__ == "__main__":
    unittest.main()
