from app.persistence.repository import quiz_repo as repo


def create(created_by: str,
           title: str,
           questions: list[repo.Question] = None
           ) -> repo.Quiz:
    data = dict(
        created_by=created_by,
        title=title
    )

    if questions:
        data["questions"] = questions

    quiz = repo.create(**data)
    add_quiz_to_user(quiz.id, created_by)
    return quiz
    # return repo.create(**data)


def get_by_id(_id: str) -> repo.Quiz:
    return repo.get_by_id(_id)


def get_all() -> list[repo.Quiz]:
    return repo.get_all()


def update_by_id(_id: str, new_data: dict) -> None:
    repo.update_by_id(_id, new_data)


def delete_by_id(_id: str) -> None:
    repo.delete_by_id(_id)


def delete_all(query: dict | None = None) -> int:
    return repo.delete_all(query)


def add_question_to_quiz(question: repo.Question, quiz: repo.Quiz) -> None:
    repo.add_question_to_quiz(question, quiz)


def has_updated_question_in_quiz(question_id: str, quiz_id: str, new_data: dict) -> bool:
    return repo.has_updated_question_in_quiz(question_id, quiz_id, new_data)


def edit_question_in_quiz(question: repo.Question,
                          quiz: repo.Quiz,
                          new_data: dict) -> None:
    return repo.edit_question_in_quiz(question, quiz, new_data)


def has_removed_question_from_quiz(question_id: str, quiz_id: str) -> bool:
    return repo.has_removed_question_from_quiz(question_id, quiz_id)


def remove_question_from_quiz(question: repo.Question, quiz: repo.Quiz) -> None:
    repo.remove_question_from_quiz(question, quiz)


def remove_all_questions(quiz: repo.Quiz) -> None:
    repo.remove_all_questions(quiz)


# region User-Quiz


def get_all_quizzes_by_username(username: str) -> list[repo.Quiz]:
    return repo.get_all_quizzes_by_username(username)


def delete_all_quizzes_by_username(username: str) -> int:
    return repo.delete_all_quizzes_by_username(username)


def add_quiz_to_user(quiz_id: str, username: str) -> None:
    return repo.add_quiz_to_user(quiz_id, username)


def remove_quiz_from_user(quiz_id: str, username: str) -> None:
    return repo.remove_quiz_from_user(quiz_id, username)

# endregion User-Quiz
