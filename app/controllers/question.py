from app.persistence.repository import question_repo as repo


def create(description: str, correct_answer: str, wrong_answers: list[str]) -> repo.Question:
    return repo.create(description=description, correct_answer=correct_answer, wrong_answers=wrong_answers)


def get_all() -> list[repo.Question]:
    return repo.get_all()


def get_by_id(_id: str) -> repo.Question:
    return repo.get_by_id(_id)


def update_by_id(_id: str, new_data: dict) -> None:
    return repo.update_by_id(_id, new_data)


def delete_by_id(_id: str) -> None:
    return repo.delete_by_id(_id)


def delete_all(query: dict | None = None) -> int:
    return repo.delete_all(query)
