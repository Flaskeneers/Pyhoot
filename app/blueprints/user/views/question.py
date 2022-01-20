from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required

from .. import bp_user
from ..forms.question import CreateQuestionForm, EditQuestionForm
from ..utils import get_clean_question_form_data, is_request_args_valid
from app.controllers import question as question_controller
from app.controllers import quiz as quiz_controller


@bp_user.get("/questions/create/<quiz_id>")
@login_required
def create_question_get(quiz_id: str):
    if quiz_controller.get_by_id(quiz_id) is None:
        flash("Quiz not found.", category="error")
        return redirect(url_for(".view_profile"))

    return render_template("user/question/create.html",
                           form=CreateQuestionForm(),
                           quiz_id=quiz_id)


@bp_user.post("/questions/create/<quiz_id>")
@login_required
def create_question_post(quiz_id: str):
    if (quiz := quiz_controller.get_by_id(quiz_id)) is None:
        flash("Quiz not found.", category="error")
        return redirect(url_for(".view_profile"))

    form = CreateQuestionForm()
    if form.validate_on_submit():
        data = get_clean_question_form_data(form.data)
        question = question_controller.create(**data)

        quiz_controller.add_question_to_quiz(question, quiz)

        flash("Question created successfully.", category="success")
        return redirect(url_for(".detail_quiz_get", quiz_id=quiz.id))
    flash("Failed to create question.", category="error")
    return render_template("user/question/create.html",
                           form=form)


@bp_user.get("/questions/detail/<question_id>")
@login_required
def detail_question_get(question_id: str):
    question = question_controller.get_by_id(question_id)
    if question is None:
        flash("Question not found.", category="error")
        return redirect(url_for(".view_profile"))
    return render_template("user/question/detail.html",
                           question=question)


@bp_user.get("/quizzes/question/edit")
@login_required
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
@login_required
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
        return redirect(url_for(".detail_quiz_get", quiz_id=quiz_id))
    else:
        return render_template("user/question/edit.html",
                               form=form,
                               question_id=question_id,
                               quiz_id=quiz_id)


@bp_user.get("/quizzes/question/delete")
@login_required
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
    return redirect(url_for(".detail_quiz_get", quiz_id=quiz_id))


@bp_user.get("/questions/delete/")
@login_required
def delete_all_questions_in_database():
    quiz_controller.delete_all()
    flash("All questions deleted.", category="success")
    return redirect(url_for(".view_profile"))
