from pymongo.collection import Collection

from .base import Document
from .quiz import Quiz
from ..db import db


class User(Document):
    collection: Collection = db.users

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @property
    def my_quizzes(self) -> list[Quiz] | None:
        from ..repository.quiz_repo import get_all_quizzes_by_username
        quizzes = get_all_quizzes_by_username(self.username)
        return quizzes if quizzes else None
