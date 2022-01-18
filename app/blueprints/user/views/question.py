from flask import flash, redirect, render_template, url_for

from .. import bp_user
from ..forms.question import CreateQuestionForm
from ..utils import get_clean_question_form_data
from app.controllers import question_controller
from app.controllers import quiz_controller


@bp_user.get("/questions/create/<quiz_id>")
def create_question_get(quiz_id: str):
    if quiz_controller.get_by_id(quiz_id) is None:
        flash("Quiz not found.", category="error")
        return redirect(url_for(".view_profile"))

    return render_template("user/question/create.html",
                           form=CreateQuestionForm(),
                           quiz_id=quiz_id)


@bp_user.post("/questions/create/<quiz_id>")
def create_question_post(quiz_id: str):
    if (quiz := quiz_controller.get_by_id(quiz_id)) is None:
        flash("Quiz not found.", category="error")
        return redirect(url_for(".view_profile"))

    form = CreateQuestionForm()
    if form.validate_on_submit():
        data = get_clean_question_form_data(form.data)
        question = question_controller.create(**data)

        # TODO: append question to quiz
        quiz_controller.add_question_to_quiz(question, quiz)

        flash("Question created successfully.", category="success")
        return redirect(url_for(".detail_question_get", question_id=question.id))
    flash("Failed to create question.", category="error")
    return render_template("user/question/create.html",
                           form=form)


@bp_user.get("/questions/detail/<question_id>")
def detail_question_get(question_id: str):
    question = question_controller.get_by_id(question_id)
    if question is None:
        flash("Question not found.", category="error")
        return redirect(url_for(".view_profile"))
    return render_template("user/question/detail.html",
                           question=question)


@bp_user.get("/questions/delete/")
def delete_all_questions():
    question_controller.delete_all()
    flash("All questions deleted.", category="success")
    return redirect(url_for(".view_profile"))
