import unittest

from app.controllers import user as user_controller
from tests import BaseTestCase


class UserTestCase(BaseTestCase):
    def test_create_user(self):
        # create a user
        email = "jane.doe@example.com"
        username = "janedoe"
        password = "super-secret-password"
        user_controller.create_user(email, username, password)

        # verify user was created in database
        user = user_controller.get_by_username(username)
        self.assertIsNotNone(user)

        self.assertEqual(user.username, username)

        user = user_controller.get_by_username("emperor-fredrik")
        self.assertIsNone(user)

        # 1. create user
        #    - assert user does exist in db
        # 2. login user
        #    - check is logged in
        # 3. logout user
        #    - check user is not logged in
        # 4. delete account
        #    - assert user no longer exists in db


if __name__ == "__main__":
    unittest.main()
