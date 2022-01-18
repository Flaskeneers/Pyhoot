from flask import flash, redirect, render_template, url_for

from . import bp_user
from .forms import CreateQuestionForm, EditQuestionForm
from app.controllers import question_controller as qc


# region Profile

@bp_user.get("/profile")
def view_profile():
    questions = qc.get_all()
    return render_template("user/profile/view.html",
                           questions=questions)


# @bp_user.get("/profile")
# def edit_profile():
#     pass


# endregion Profile


# region Question

def get_clean_question_form_data(form_data: dict) -> dict:
    return dict(
        description=form_data["description"],
        correct_answer=form_data["correct_answer"]["text"],
        wrong_answers=[wrong_answer["text"] for wrong_answer
                       in form_data["wrong_answers"]]
    )


@bp_user.get("/questions")
def create_question_get():
    return render_template("user/question/create.html",
                           form=CreateQuestionForm())


@bp_user.post("/questions")
def create_question_post():
    form = CreateQuestionForm()
    if form.validate_on_submit():
        data = get_clean_question_form_data(form.data)
        question = qc.create(**data)
        flash("Question created successfully.", category="success")
        return redirect(url_for(".detail_question_get", question_id=question.id))
    flash("Failed to create question.", category="error")
    return render_template("user/question/create.html",
                           form=form)


@bp_user.get("/questions/detail/<question_id>")
def detail_question_get(question_id: str):
    question = qc.get_by_id(question_id)
    if question is None:
        flash("Question not found.", category="error")
        return redirect(url_for(".view_profile"))
    return render_template("user/question/detail.html",
                           question=question)


@bp_user.get("/questions/edit/<question_id>")
def edit_question_get(question_id: str):
    question = qc.get_by_id(question_id)
    form = EditQuestionForm(obj=question)
    return render_template("user/question/edit.html",
                           form=form)


@bp_user.post("/questions/edit/<question_id>")
def edit_question_post(question_id: str):
    form = EditQuestionForm()
    if form.validate_on_submit():
        if qc.get_by_id(question_id) is None:
            flash("Question not found.", category="error")
        else:
            data = get_clean_question_form_data(form.data)
            qc.update_by_id(question_id, data)

            flash("Question updated successfully.", category="success")
            return redirect(url_for(".view_profile"))

    flash("Failed to update question.", category="error")
    return render_template("user/question/edit.html",
                           form=form)


@bp_user.get("/questions/delete/<question_id>")
def delete_question(question_id: str):
    if qc.get_by_id(question_id) is None:
        flash("Question not found.", category="error")
    else:
        qc.delete_by_id(question_id)
        flash("Question deleted successfully.", category="success")
    return redirect(url_for(".view_profile"))


@bp_user.get("/questions/delete")
def delete_all_questions():
    qc.delete_all()
    flash("All questions deleted.", category="success")
    return redirect(url_for(".view_profile"))


# endregion Question


# region Quiz


@bp_user.get("/quizzes")
def create_quiz_get():
    pass


@bp_user.post("/quizzes")
def create_quiz_post():
    pass


@bp_user.get("/quizzes/detail/<quiz_id>")
def detail_quiz_get():
    pass


@bp_user.get("/quizzes/edit/<quiz_id>")
def edit_quiz_get():
    pass


@bp_user.put("/quizzes/edit/<quiz_id>")
def edit_quiz_post():
    pass


@bp_user.delete("/quizzes/delete/<quiz_id>")
def delete_quiz():
    pass

# endregion Quiz
