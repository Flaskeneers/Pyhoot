from flask import flash, redirect, render_template, request, url_for

from .. import bp_user
from ..forms.question import EditQuestionForm
from ..forms.quiz import CreateQuizForm, EditQuizForm
from app.controllers import question_controller, quiz_controller


# region Quiz
from ..utils import get_clean_question_form_data


@bp_user.get("/quizzes")
def create_quiz_get():
    return render_template("user/quiz/create.html",
                           form=CreateQuizForm())


@bp_user.post("/quizzes")
def create_quiz_post():
    form = CreateQuizForm()
    if form.validate_on_submit():
        # TODO: get real username from current_user
        username = "pyhoot-master"
        title = form.title.data
        quiz = quiz_controller.create(created_by=username, title=title)
        flash("Quiz created successfully.", category="success")
        return redirect(url_for(".detail_quiz_get", quiz_id=quiz.id))
    flash("Failed to create quiz.", category="error")
    return render_template("user/quiz/create.html",
                           form=form)


@bp_user.get("/quizzes/detail/<quiz_id>")
def detail_quiz_get(quiz_id: str):
    quiz = quiz_controller.get_by_id(quiz_id)
    if quiz is None:
        flash("Question not found.", category="error")
        return redirect(url_for(".view_profile"))
    return render_template("user/quiz/detail.html",
                           quiz=quiz)


@bp_user.get("/quizzes/edit/<quiz_id>")
def edit_quiz_get(quiz_id: str):
    quiz = quiz_controller.get_by_id(quiz_id)
    form = EditQuizForm(obj=quiz)
    return render_template("user/quiz/edit.html",
                           form=form)


@bp_user.post("/quizzes/edit/<quiz_id>")
def edit_quiz_post(quiz_id: str):
    form = EditQuizForm()
    if form.validate_on_submit():
        if quiz_controller.get_by_id(quiz_id) is None:
            flash("Quiz not found.", category="error")
        else:
            quiz_controller.update_by_id(quiz_id, new_data={"title": form.title.data})
            flash("Quiz updated successfully.", category="success")
            return redirect(url_for(".view_profile"))

    flash("Failed to update quiz.", category="error")
    return render_template("user/quiz/edit.html",
                           form=form)


# TODO: only owner or admin should be able to delete
@bp_user.get("/quizzes/delete/<quiz_id>")
def delete_quiz(quiz_id: str):
    if quiz_controller.get_by_id(quiz_id) is None:
        flash("Quiz not found.", category="error")
    else:
        quiz_controller.delete_by_id(quiz_id)
        flash("Quiz deleted successfully.", category="success")
    return redirect(url_for(".view_profile"))


@bp_user.get("/quizzes/delete")
def delete_all_quizzes():
    quiz_controller.delete_all()
    flash("All quizzes deleted.", category="success")
    return redirect(url_for(".view_profile"))


# endregion Quiz


# region Quiz-Question

@bp_user.get("/quizzes/question/edit")
def edit_question_in_quiz_get():
    question_id = request.args.get("question_id")
    quiz_id = request.args.get("quiz_id")

    if not is_request_args_valid(question_id, quiz_id):
        flash("Invalid request args.", category="error")
        return redirect(url_for(".view_profile"))

    question = question_controller.get_by_id(question_id)
    quiz = quiz_controller.get_by_id(quiz_id)

    if question is None or quiz is None:
        flash("Question and/or Quiz not found.", category="error")
        return redirect(url_for(".view_profile"))

    form = EditQuestionForm(obj=question)
    return render_template("user/question/edit.html",
                           form=form,
                           question_id=question_id,
                           quiz_id=quiz_id)


@bp_user.post("/quizzes/question/edit")
def edit_question_in_quiz_post():
    question_id = request.args.get("question_id")
    quiz_id = request.args.get("quiz_id")

    if not is_request_args_valid(question_id, quiz_id):
        flash("Invalid request args.", category="error")
        return redirect(url_for(".view_profile"))

    question = question_controller.get_by_id(question_id)
    quiz = quiz_controller.get_by_id(quiz_id)

    if question is None or quiz is None:
        flash("Question and/or Quiz not found.", category="error")
        return redirect(url_for(".view_profile"))

    form = EditQuestionForm()
    if form.validate_on_submit():
        new_data = get_clean_question_form_data(form.data)
        quiz_controller.edit_question_in_quiz(question, quiz, new_data)
        flash("Question edited successfully.", category="success")
        return redirect(url_for(".view_profile"))
    else:
        return render_template("user/question/edit.html",
                               form=form,
                               question_id=question_id,
                               quiz_id=quiz_id)


@bp_user.get("/quizzes/question/delete")
def delete_question_in_quiz():
    question_id = request.args.get("question_id")
    quiz_id = request.args.get("quiz_id")

    if not is_request_args_valid(question_id, quiz_id):
        flash("Invalid request args.", category="error")
        return redirect(url_for(".view_profile"))

    question = question_controller.get_by_id(question_id)
    quiz = quiz_controller.get_by_id(quiz_id)

    # TODO: edit and delete reuse this in controller/repo function
    if question is None or quiz is None:
        flash("Question and/or Quiz not found.", category="error")
        return redirect(url_for(".view_profile"))

    quiz_controller.remove_question_from_quiz(question, quiz)
    flash("Question deleted successfully.", category="success")
    return redirect(url_for(".view_profile"))


@bp_user.get("/quizzes/delete/questions/<quiz_id>")
def delete_all_questions_in_quiz(quiz_id: str):
    if (quiz := quiz_controller.get_by_id(quiz_id)) is None:
        flash("Quiz not found.", category="error")
    else:
        quiz_controller.remove_all_questions(quiz)
        flash("Quiz questions deleted successfully.", category="success")
    return redirect(url_for(".view_profile"))


def is_request_args_valid(question_id: str, quiz_id: str) -> bool:
    return question_id is not None and quiz_id is not None

# endregion Quiz-Question
