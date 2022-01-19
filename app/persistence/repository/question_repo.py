from bson import ObjectId

from app.persistence.models.question import Question
from app.shared.resultlist import ResultList


def create(**kwargs) -> Question:
    question = Question(kwargs)
    question.save()
    return question


def get_all() -> list[Question]:
    return ResultList(Question(item) for item in Question.find())


def get_by_id(_id: str) -> Question | None:
    return ResultList(Question(item) for item in
                      Question.collection.find(dict(_id=ObjectId(_id)))).first_or_none()


def update_by_id(_id: str, new_data: dict) -> None:
    question = get_by_id(_id)
    question.update_with(new_data)


def delete_by_id(_id: str) -> None:
    question = get_by_id(_id)
    if question is not None:
        question.delete()


def delete_all(query: dict | None = None) -> int:
    result = Question.collection.delete_many(query if query else {})
    return result.deleted_count
