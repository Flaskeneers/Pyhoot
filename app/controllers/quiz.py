from app.persistence.repository import quiz_repo as repo


def create(created_by: str,
           title: str,
           questions: list[repo.Question] = None
           ) -> repo.Quiz:
    return repo.create(created_by=created_by,
                       title=title,
                       questions=questions)


def get_all() -> list[repo.Quiz]:
    return repo.get_all()


def get_all_by_username(username: str) -> list[repo.Quiz]:
    return repo.get_all_by_username(username)


def delete_all_by_username(username: str) -> int:
    return repo.delete_all_by_username(username)


def get_by_id(_id: str) -> repo.Quiz:
    return repo.get_by_id(_id)


def update_by_id(_id: str, new_data: dict) -> None:
    repo.update_by_id(_id, new_data)


def delete_by_id(_id: str) -> None:
    repo.delete_by_id(_id)


def delete_all(query: dict | None = None) -> int:
    return repo.delete_all(query)


def add_question_to_quiz(question: repo.Question, quiz: repo.Quiz) -> None:
    repo.add_question_to_quiz(question, quiz)


def edit_question_in_quiz(question: repo.Question,
                          quiz: repo.Quiz,
                          new_data: dict) -> None:
    return repo.edit_question_in_quiz(question, quiz, new_data)


def remove_question_from_quiz(question: repo.Question, quiz: repo.Quiz) -> None:
    repo.remove_question_from_quiz(question, quiz)


def remove_all_questions(quiz: repo.Quiz) -> None:
    repo.remove_all_questions(quiz)
