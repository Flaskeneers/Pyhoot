from flask import render_template

from .forms import SignupForm, LoginForm
from app.persistence.repository.user_repo import create_user, get_by_username, check_existing_users, verify_password
from . import bp_auth


@bp_auth.route("/signup", methods=['GET', 'POST'])
def signup():

    username = None
    password = None

    form = SignupForm()

    # If all fields in form is correct...
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        if check_existing_users(username, email):
            create_user(email, username, password)

    return render_template("auth/signup.html", username=username, password=password, form=form)


@bp_auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if get_by_username(username) is not None:
            if verify_password(username, password):
                return render_template("auth/login.html", form=form, username=username)

            else:
                print('Invalid Credentials')

        else:
            print('Invalid Credentials')

    return render_template("auth/login.html", form=form)
