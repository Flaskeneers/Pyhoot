from flask import render_template, flash

from . import bp_auth
from .forms import SignupForm, LoginForm
from app.persistence.repository.user_repo import create_user, get_by_username, check_existing_users, verify_password


@bp_auth.route("/signup/", methods=['GET', 'POST'])
def signup():

    username = None
    form = SignupForm()

    # If all fields in form is correct...
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        if check_existing_users(username, email):
            create_user(email, username, password)
            flash('User Created!')
        else:
            flash('Username Already Exists')

    return render_template("auth/signup.html", username=username, form=form)


@bp_auth.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if get_by_username(username) is not None:
            if verify_password(username, password):
                return render_template("auth/user.html", form=form, username=username)

            else:
                flash('Invalid Credentials')

        else:
            flash('Invalid Credentials')

    return render_template("auth/login.html", form=form)


