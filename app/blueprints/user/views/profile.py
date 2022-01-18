from flask import flash, redirect, render_template, url_for

from .. import bp_user
from app.controllers import question_controller as qc


@bp_user.get("/profile")
def view_profile():
    questions = qc.get_all()
    return render_template("user/profile/view.html",
                           questions=questions)

# @bp_user.get("/profile")
# def edit_profile():
#     pass
