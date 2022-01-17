from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import EqualTo, Length, InputRequired


class SignupForm(FlaskForm):

    username = StringField('Username: ', validators=[InputRequired(),
                                                     Length(3, 25)])
    password = PasswordField('Password: ', validators=[InputRequired(),
                                                       Length(3)])
    repeat_pass = PasswordField('Repeat Password:', validators=[InputRequired(message='Password Required'),
                                                                EqualTo('password', message='Passwords must match')])
    create_user = SubmitField('Sign up!')


class LoginForm(FlaskForm):

    username = StringField('username_label',
                           validators=[InputRequired(message='username required')])
    password = PasswordField('password_label',
                             validators=[InputRequired(message='password required')])
    submit_button = SubmitField('Login')
