from bson import ObjectId

from app.persistence.models.question import Question
from app.shared.resultlist import ResultList


def create(description: str, correct_answer: str, wrong_answers: list[str]) -> Question:
    data = dict(
        description=description,
        correct_answer=correct_answer,
        wrong_answers=wrong_answers
    )
    question = Question(data)
    question.save()
    return question


def get_all() -> list[Question]:
    return ResultList(Question(item) for item in Question.collection.find())


def get_by_id(_id: str) -> Question:
    return ResultList(Question(item) for item in Question.collection.find(dict(_id=ObjectId(_id)))).first_or_none()


def delete_all(query: dict | None = None) -> int:
    result = Question.collection.delete_many(query if query else {})
    return result.deleted_count
