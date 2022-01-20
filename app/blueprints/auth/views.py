from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

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

        user = get_by_username(username)

        if user is not None:
            if verify_password(user.password, password):
                login_user(user)
                flash(user.email)
                flash(user.username)

                return redirect(url_for("user.view_profile"))

            else:
                flash('Invalid Credentials')

        else:
            flash('Invalid Credentials')

    return render_template("auth/login.html", form=form)


@bp_auth.get('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('guest.index'))
