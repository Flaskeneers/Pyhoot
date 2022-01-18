from app.persistence.repository import quiz_repo as repo


def create(questions: list[repo.Question],
           created_by: str = None) -> repo.Quiz:
    return repo.create(questions=questions,
                       created_by=created_by)


def get_all() -> list[repo.Quiz]:
    return repo.get_all()


def get_by_id(_id: str) -> repo.Quiz:
    return repo.get_by_id(_id)


def update_by_id(_id: str, new_data: dict) -> None:
    return repo.update_by_id(_id, new_data)


def delete_by_id(_id: str) -> None:
    return repo.delete_by_id(_id)


def delete_all(query: dict | None = None) -> int:
    return repo.delete_all(query)
