from app.persistence.models.question import Question
from app.persistence.models.quiz import Quiz
from app.persistence.repository.base import BaseRepository, ResultList


class QuizRepository(BaseRepository):
    document = Quiz

    @classmethod
    def get_all_by_username(cls, username: str) -> list[Quiz] | None:
        return cls._find(many=True, username=username)

    @classmethod
    def delete_all_by_username(cls, username: str) -> int:
        delete_count = 0
        quizzes = cls.get_all_by_username(username)

        for quiz in quizzes:
            for question in quiz.questions:
                question.delete()

            quiz.delete()
            delete_count += 1

        return delete_count

    @classmethod
    def add_question_to_quiz(cls, question: Question, quiz: Quiz) -> None:
        pass

    @classmethod
    def edit_question_in_quiz(cls, question: Question,
                              quiz: Quiz,
                              new_data: dict) -> None:
        pass

    @classmethod
    def remove_question_from_quiz(cls, question: Question, quiz: Quiz) -> None:
        pass

    @classmethod
    def remove_all_questions(cls, quiz: Quiz) -> None:
        pass

    @classmethod
    def add_question_to_quiz(cls, question: Question, quiz: Quiz) -> None:
        if not quiz.get("questions", None):
            quiz.questions = []

        if not cls.has_question(question.id, quiz):
            quiz.questions.append(question.__dict__)
            quiz.save()

    @classmethod
    def edit_question_in_quiz(cls, question: Question,
                              quiz: Quiz,
                              new_data: dict) -> None:
        if not cls.has_questions(quiz):
            return

        for index, question_dict in enumerate(quiz.questions):
            if question_dict["_id"] == question._id:
                cls.update_by_id(question.id, new_data)

                quiz.questions[index].update(new_data)
                quiz.save()
                return

    @classmethod
    def remove_question_from_quiz(cls, question: Question, quiz: Quiz) -> None:
        if not cls.has_questions(quiz):
            return

        for index, question_dict in enumerate(quiz.questions):
            if question_dict["_id"] == question._id:
                cls.delete_by_id(question.id)

                quiz.questions.pop(index)
                if cls.is_questions_empty(quiz.questions):
                    del quiz.questions

                quiz.save()
                return

    @classmethod
    def remove_all_questions(cls, quiz: Quiz) -> None:
        if not cls.has_questions(quiz):
            return

        for question_dict in quiz.questions:
            question = QuestionRepository.get_by_id(question_dict["_id"])
            cls.remove_question_from_quiz(question, quiz)

    @classmethod
    def has_question(cls, question_id: str, quiz: Quiz) -> bool:
        for question in quiz.questions:
            if question["_id"] == question_id:
                return True
        return False

    @classmethod
    def has_questions(cls, quiz: Quiz) -> bool:
        return hasattr(quiz, "questions")

    @classmethod
    def is_questions_empty(cls, questions: list) -> bool:
        return questions == []

# def create(created_by: str,
#            title: str,
#            questions: list[Question] = None
#            ) -> Quiz:
#     data = dict(
#         created_by=created_by,
#         title=title,
#     )
#
#     if questions:
#         data["questions"] = questions
#
#     quiz = Quiz(data)
#     quiz.save()
#     return quiz


# def get_all() -> list[Quiz]:
#     return ResultList(Quiz(item) for item in Quiz.collection.find())


# TODO:
# def get_all_by_username(username: str) -> list[Quiz]:
#     return ResultList(Quiz(item) for item in Quiz.collection.find(dict(created_by=username)))
#
#
# # TODO:
# def delete_all_by_username(username: str) -> int:
#     quizzes = get_all_by_username(username)
#
#     if not quizzes:
#         return 0
#
#     for quiz in quizzes:
#         if has_questions(quiz):
#             for question in quiz.questions:
#                 question_repo.delete_by_id(question["_id"])
#
#     return delete_all(dict(created_by=username))


# def get_by_id(_id: str) -> Quiz:
#     return ResultList(Quiz(item) for item in Quiz.collection.find(dict(_id=ObjectId(_id)))).first_or_none()


# def update_by_id(_id: str, new_data: dict) -> None:
#     quiz = get_by_id(_id)
#     quiz.update_with(new_data)
#
#
# def delete_by_id(_id: str) -> None:
#     quiz = get_by_id(_id)
#     remove_all_questions(quiz)
#     quiz.delete()


# def delete_all(query: dict | None = None) -> int:
#     result = Quiz.collection.delete_many(query if query else {})
#     return result.deleted_count


# def add_question_to_quiz(question: Question, quiz: Quiz) -> None:
#     if not quiz.get("questions", None):
#         quiz.questions = []
#
#     if not has_question(question.id, quiz):
#         quiz.questions.append(question.__dict__)
#         quiz.save()
#
#
# def edit_question_in_quiz(question: Question,
#                           quiz: Quiz,
#                           new_data: dict) -> None:
#     if not has_questions(quiz):
#         return
#
#     for index, question_dict in enumerate(quiz.questions):
#         if question_dict["_id"] == question._id:
#             question_repo.update_by_id(question.id, new_data)
#
#             quiz.questions[index].update(new_data)
#             quiz.save()
#             return
#
#
# def remove_question_from_quiz(question: Question, quiz: Quiz) -> None:
#     if not has_questions(quiz):
#         return
#
#     for index, question_dict in enumerate(quiz.questions):
#         if question_dict["_id"] == question._id:
#             question_repo.delete_by_id(question.id)
#
#             quiz.questions.pop(index)
#             if is_questions_empty(quiz.questions):
#                 del quiz.questions
#
#             quiz.save()
#             return
#
#
# def remove_all_questions(quiz: Quiz) -> None:
#     if not has_questions(quiz):
#         return
#
#     for question_dict in quiz.questions:
#         question = question_repo.get_by_id(question_dict["_id"])
#         remove_question_from_quiz(question, quiz)
#
#
# def has_question(question_id: str, quiz: Quiz) -> bool:
#     for question in quiz.questions:
#         if question["_id"] == question_id:
#             return True
#     return False
#
#
# def has_questions(quiz: Quiz) -> bool:
#     return hasattr(quiz, "questions")
#
#
# def is_questions_empty(questions: list) -> bool:
#     return questions == []
