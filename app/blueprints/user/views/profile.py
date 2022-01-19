from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from .. import bp_user
from ..forms.profile import EditProfileForm
from app.controllers import quiz as quiz_controller


@bp_user.get("/profile")
@login_required
def view_profile():
    quizzes = quiz_controller.get_all_by_username(current_user.username)
    return render_template("user/profile/view.html",
                           quizzes=quizzes)

# @bp_user.get("/profile")
# def edit_profile():
#     pass
