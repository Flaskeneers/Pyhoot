from bson import ObjectId

from app.persistence.models.question import Question
from app.persistence.models.quiz import Quiz
from app.shared.resultlist import ResultList


# created_by = user.username?  # dependent on get_by_username
def create(questions: list[Question], created_by: str = None) -> Quiz:
    data = dict(
        questions=questions,
        created_by=created_by
    )
    quiz = Quiz(data)
    quiz.save()
    return quiz


def get_all() -> list[Quiz]:
    return ResultList(Quiz(item) for item in Quiz.collection.find())


def get_by_id(_id: str) -> Quiz:
    return ResultList(Quiz(item) for item in Quiz.collection.find(dict(_id=ObjectId(_id)))).first_or_none()


def update_by_id(_id: str, new_data: dict) -> None:
    quiz = get_by_id(_id)
    quiz.update_with(new_data)


def delete_by_id(_id: str) -> None:
    quiz = get_by_id(_id)
    quiz.delete()


def delete_all(query: dict | None = None) -> int:
    result = Quiz.collection.delete_many(query if query else {})
    return result.deleted_count
