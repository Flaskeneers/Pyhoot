import unittest

from tests import BaseTestCase


class QuizTestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        # additional dependencies for testing quiz
        from app.controllers import quiz as quiz_controller
        cls.quiz_controller = quiz_controller

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_create_quiz(self):
        pass

    def test_edit_quiz(self):
        pass

    def test_add_questions_to_quiz(self):
        pass
