from flask import render_template, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

import app
from . import bp_auth
from .forms import SignupForm, LoginForm, UpdateForm
from ...controllers import user as user_controller
from ...controllers.user import get_by_username

from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import datetime


@bp_auth.route("/signup/", methods=['GET', 'POST'])
def signup():
    username = None
    form = SignupForm()
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    # If all fields in form is correct...
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        token = serializer.dumps(email)

        if user_controller.check_existing_users(username, email):

            user_controller.create_user(email, username, password)

            msg = Message('Confirmed Email', sender=current_app.config["MAIL_SENDER"], recipients=[email])
            link = url_for('auth.confirm_email', token=token, _external=True)
            msg.body = 'Verify Email: {}'.format(link)

            app.mail.send(msg)

            flash('User Created! A verification link has been sent to your email account')
        else:
            flash('Username Already Exists')

    return render_template("auth/signup.html", username=username, form=form)


@bp_auth.route('/confirm/<token>')
def confirm_email(token):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    try:
        email = serializer.loads(token, max_age=3600)
    except:
        return '<h1>The confirmation link is invalid or has expired...</h1>'

    user = user_controller.get_by_email(email)

    if user.is_confirmed:
        flash('Account already confirmed')
    else:
        user.is_confirmed = True
        user.is_confirmed_since = datetime.datetime.now()
        user.save()

        flash('You have confirmed your account. Thanks!')
        return redirect(url_for('auth.login'))

    return render_template('guest/index.html')


@bp_auth.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = user_controller.get_by_username(username)

        if user is not None:
            if user_controller.verify_password(user, password):
                if user.is_confirmed:
                    login_user(user)
                    flash(user.email)
                    flash(user.username)

                    return redirect(url_for("user.view_profile", username=user.username))
                else:
                    flash('Please verify your email before logging in')

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


@bp_auth.route('/update/<string:username>', methods=['GET', 'POST'])
@login_required
def update(username):
    form = UpdateForm()

    email = form.email.data
    new_password = form.new_password.data
    password = form.password.data

    user = get_by_username(username)

    if form.validate_on_submit():
        if user_controller.verify_password(user, password):
            user_controller.update_by_username(current_user.username, new_data={"email": email})
            user_controller.update_by_username(current_user.username, new_data={"password": generate_password_hash
                                                                                (new_password)})
            user_controller.update_by_username(current_user.username, new_data={"first_name": form.first_name.data})
            user_controller.update_by_username(current_user.username, new_data={"country": form.country.data})

            flash('User Updated Successfully!')

            return redirect(url_for('guest.index'))

        else:
            flash('Invalid Credentials')

    return render_template("auth/update.html", form=form)
