from bson import ObjectId

from app.persistence.models.question import Question
from app.persistence.models.quiz import Quiz
from app.persistence.models.user import User
from app.persistence.repository import question_repo
from app.persistence.repository import user_repo
from app.shared.resultlist import ResultList


# region Quiz

def create(**kwargs) -> Quiz:
    quiz = Quiz(kwargs)
    quiz.save()
    return quiz


def get_by_id(_id: str) -> Quiz | None:
    return Quiz(Quiz.collection.find_one(dict(_id=ObjectId(_id))))


def get_all() -> list[Quiz]:
    return ResultList(Quiz(item) for item in Quiz.find())


def update_by_id(_id: str, new_data: dict) -> None:
    quiz = get_by_id(_id)
    quiz.update_with(new_data)


def delete_by_id(_id: str) -> None:
    quiz = get_by_id(_id)
    remove_all_questions(quiz)
    remove_quiz_from_user(quiz.id, quiz.created_by)
    quiz.delete()


def delete_all(query: dict | None = None) -> int:
    result = Quiz.collection.delete_many(query if query else {})
    return result.deleted_count


# endregion Quiz


# region Quiz-Question

def add_question_to_quiz(question: Question, quiz: Quiz) -> None:
    if not quiz.get("questions", None):
        quiz.questions = []

    if not has_question(question.id, quiz):
        quiz.questions.append(question.__dict__)
        quiz.save()


def edit_question_in_quiz(question: Question,
                          quiz: Quiz,
                          new_data: dict) -> None:
    if not has_questions(quiz):
        return

    for index, question_dict in enumerate(quiz.questions):
        if question_dict["_id"] == question._id:
            question_repo.update_by_id(question.id, new_data)

            quiz.questions[index].update(new_data)
            quiz.save()
            return


def remove_question_from_quiz(question: Question, quiz: Quiz) -> None:
    if not has_questions(quiz):
        return

    for index, question_dict in enumerate(quiz.questions):
        if question_dict["_id"] == question._id:
            question_repo.delete_by_id(question._id)

            quiz.questions.pop(index)
            if is_questions_empty(quiz.questions):
                del quiz.questions

            quiz.save()
            return


def remove_all_questions(quiz: Quiz) -> None:
    if not has_questions(quiz):
        return

    for question_dict in quiz.questions:
        question = question_repo.get_by_id(question_dict["_id"])
        remove_question_from_quiz(question, quiz)


def has_question(question_id: str, quiz: Quiz) -> bool:
    for question in quiz.questions:
        if question["_id"] == question_id:
            return True
    return False


def has_questions(quiz: Quiz) -> bool:
    return hasattr(quiz, "questions")


def is_questions_empty(questions: list) -> bool:
    return questions == []


# endregion Quiz-Question


# region User-Quiz


def get_all_quizzes_by_username(username: str) -> list[Quiz]:
    return ResultList(Quiz(item) for item in Quiz.collection.find(dict(created_by=username)))


def delete_all_quizzes_by_username(username: str) -> int:
    quizzes = get_all_quizzes_by_username(username)

    if not quizzes:
        return 0

    for quiz in quizzes:
        if has_questions(quiz):
            for question_dict in quiz.questions:
                question_repo.delete_by_id(question_dict["_id"])

        remove_quiz_from_user(quiz.id, username)

    return delete_all(dict(created_by=username))


def has_quiz(quiz_id: str, user: User) -> bool:
    return quiz_id in user.quizzes


def has_quizzes(user: User) -> bool:
    return hasattr(user, "quizzes")


def add_quiz_to_user(quiz_id: str, username: str) -> None:
    user = user_repo.get_by_username(username)

    if not user:
        return None

    if not hasattr(user, "quizzes"):
        user.quizzes = []

    if has_quiz(quiz_id, user):
        return

    user.quizzes.append(quiz_id)
    user.save()


def remove_quiz_from_user(quiz_id: str, username: str) -> None:
    user = user_repo.get_by_username(username)
    if not user or not has_quizzes(user) or not has_quiz(quiz_id, user):
        return

    for index, _id in enumerate(user.quizzes):
        if _id == quiz_id:
            user.quizzes.pop(index)

            if not user.quizzes:
                del user.quizzes

            user.save()

# endregion User-Quiz
