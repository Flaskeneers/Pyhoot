from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from .. import bp_user
from ..forms.quiz import CreateQuizForm, EditQuizForm
from app.controllers import quiz as quiz_controller


@bp_user.get("/quizzes")
@login_required
def create_quiz_get():
    return render_template("user/quiz/create.html",
                           form=CreateQuizForm())


@bp_user.post("/quizzes")
@login_required
def create_quiz_post():
    form = CreateQuizForm()
    if form.validate_on_submit():
        quiz = quiz_controller.create(created_by=current_user.username, title=form.title.data)
        flash("Quiz created successfully.", category="success")
        return redirect(url_for(".detail_quiz_get", quiz_id=quiz.id))
    flash("Failed to create quiz.", category="error")
    return render_template("user/quiz/create.html",
                           form=form)


@bp_user.get("/quizzes/detail/<quiz_id>")
@login_required
def detail_quiz_get(quiz_id: str):
    quiz = quiz_controller.get_by_id(quiz_id)
    if quiz is None:
        flash("Question not found.", category="error")
        return redirect(url_for(".view_profile"))
    return render_template("user/quiz/detail.html",
                           quiz=quiz)


@bp_user.get("/quizzes/edit/<quiz_id>")
@login_required
def edit_quiz_get(quiz_id: str):
    quiz = quiz_controller.get_by_id(quiz_id)
    form = EditQuizForm(obj=quiz)
    return render_template("user/quiz/edit.html",
                           form=form)


@bp_user.post("/quizzes/edit/<quiz_id>")
@login_required
def edit_quiz_post(quiz_id: str):
    form = EditQuizForm()
    if form.validate_on_submit():
        if quiz_controller.get_by_id(quiz_id) is None:
            flash("Quiz not found.", category="error")
        else:
            quiz_controller.update_by_id(quiz_id, new_data={"title": form.title.data})
            flash("Quiz updated successfully.", category="success")
            return redirect(url_for(".detail_quiz_get", quiz_id=quiz_id))

    flash("Failed to update quiz.", category="error")
    return render_template("user/quiz/edit.html",
                           form=form)


# TODO: only owner or admin should be able to delete
@bp_user.get("/quizzes/delete/<quiz_id>")
@login_required
def delete_quiz(quiz_id: str):
    if quiz_controller.get_by_id(quiz_id) is None:
        flash("Quiz not found.", category="error")
    else:
        quiz_controller.delete_by_id(quiz_id)
        # quiz_controller.remove_quiz_from_user(quiz_id, current_user.username)
        flash("Quiz deleted successfully.", category="success")
    return redirect(url_for(".view_profile"))


@bp_user.get("/quizzes/delete")
@login_required
def delete_my_quizzes():
    deleted_quizzes = quiz_controller.delete_all_quizzes_by_username(current_user.username)
    flash(f"{deleted_quizzes} quizzes deleted.", category="success")
    return redirect(url_for(".view_profile"))


@bp_user.get("/quizzes/delete/questions/<quiz_id>")
@login_required
def delete_all_questions_in_quiz(quiz_id: str):
    if (quiz := quiz_controller.get_by_id(quiz_id)) is None:
        flash("Quiz not found.", category="error")
    else:
        quiz_controller.remove_all_questions(quiz)
        flash("Quiz questions deleted successfully.", category="success")
    return redirect(url_for(".detail_quiz_get", quiz_id=quiz_id))


@bp_user.get("/quizzes/delete/all")
@login_required
def delete_all_quizzes_in_database():
    quiz_controller.delete_all()
    flash("All quizzes deleted.", category="success")
    return redirect(url_for(".view_profile"))
