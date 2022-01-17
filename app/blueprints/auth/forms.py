from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Length, InputRequired, Email


class SignupForm(FlaskForm):

    email = StringField('E-mail: ', validators=[InputRequired(),
                                                Email(message='please enter a valid Email')])

    username = StringField('Username: ', validators=[InputRequired(), Length(3, 25)])
    password = PasswordField('Password: ', validators=[InputRequired(), Length(3, 30)])
    repeat_pass = PasswordField('Repeat Password:', validators=[InputRequired()])

    create_user = SubmitField('Sign up!')


class LoginForm(FlaskForm):

    username = StringField('Username: ', validators=[InputRequired()])
    password = PasswordField('Password: ', validators=[InputRequired()])

    login_button = SubmitField('Login')
