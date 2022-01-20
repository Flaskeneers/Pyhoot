from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from .. import bp_user
from ..forms.profile import EditProfileForm


@bp_user.get("/profile")
@login_required
def view_profile():
    return render_template("user/profile/view.html",
                           quizzes=current_user.my_quizzes)

# @bp_user.get("/profile")
# def edit_profile():
#     pass
