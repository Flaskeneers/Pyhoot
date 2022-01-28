from http import HTTPStatus

from flask import abort, render_template

from .. import bp_user
from ..forms.profile import EditProfileForm
from app.controllers import quiz as quiz_controller
from app.controllers import user as user_controller


@bp_user.get("/profile/<username>")
def view_profile(username: str):
    if not user_controller.get_by_username(username):
        abort(HTTPStatus.NOT_FOUND, "This is not the profile you are looking for.")

    quizzes = quiz_controller.get_all_quizzes_by_username(username)
    return render_template("user/profile/view.html",
                           quizzes=quizzes)


# TODO: should only be accessible if logged in and it is current_users own profile
# @bp_user.get("/profile")
# def edit_profile():
#     pass
