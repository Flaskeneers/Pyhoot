from flask import flash, redirect, render_template, url_for

from .. import bp_user
from ..forms.profile import EditProfileForm
from app.controllers import quiz as quiz_controller


@bp_user.get("/profile")
def view_profile():
    quizzes = quiz_controller.get_all_quizzes_by_username(current_user.username)
    return render_template("user/profile/view.html",
                           quizzes=quizzes)

# @bp_user.get("/profile")
# def edit_profile():
#     pass
