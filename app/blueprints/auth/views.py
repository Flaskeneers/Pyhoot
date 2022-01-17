from flask import render_template
from .forms import SignupForm, LoginForm

from . import bp_auth


@bp_auth.route("/signup", methods=['GET', 'POST'])
def signup():
    username = None
    password = None
    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        form.username.data = ''
        form.password.data = ''
        print('Success')

    return render_template("auth/signup.html",
                           username=username,
                           password=password,
                           form=form)


@bp_auth.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template("auth/login.html",
                           form=form)
