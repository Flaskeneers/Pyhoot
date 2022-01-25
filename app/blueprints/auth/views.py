from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

from . import bp_auth
from .forms import SignupForm, LoginForm, UpdateForm
from ...controllers import user as user_controller


@bp_auth.route("/signup/", methods=['GET', 'POST'])
def signup():
    username = None
    form = SignupForm()

    # If all fields in form is correct...
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        if user_controller.check_existing_users(username, email):
            user_controller.create_user(email, username, password)
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

        user = user_controller.get_by_username(username)

        if user is not None:
            if user_controller.verify_password(user, password):
                login_user(user)
                flash(user.email)
                flash(user.username)

                return redirect(url_for("user.view_profile", username=user.username))

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


@bp_auth.route('/update/', methods=['GET', 'POST'])
@login_required
def update():
    form = UpdateForm()
    email = form.email.data
    new_password = form.new_password.data

    if form.validate_on_submit():
        user_controller.update_by_username(current_user.username, new_data={"email": email})
        user_controller.update_by_username(current_user.username, new_data={"password": generate_password_hash
                                                                            (new_password)})

        return redirect(url_for('guest.index'))

    return render_template("auth/update.html", form=form)
