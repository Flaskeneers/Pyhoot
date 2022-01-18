from flask import flash, redirect, render_template, url_for

from .. import bp_user
from ..forms.profile import EditProfileForm
from app.controllers import question_controller
from app.controllers import quiz_controller


@bp_user.get("/profile")
def view_profile():
    questions = question_controller.get_all()
    quizzes = quiz_controller.get_all()
    return render_template("user/profile/view.html",
                           questions=questions,
                           quizzes=quizzes)

# @bp_user.get("/profile")
# def edit_profile():
#     pass
