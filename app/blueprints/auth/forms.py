from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import EqualTo, Length, InputRequired, Email, ValidationError


class SignupForm(FlaskForm):

    email = StringField('E-mail: ', validators=[InputRequired(),
                                                Email(message='please enter a valid Email')])

    username = StringField('Username: ', validators=[InputRequired(),
                                                     Length(3, 25)])
    password = PasswordField('Password: ', validators=[InputRequired(),
                                                       Length(3)])
    repeat_pass = PasswordField('Repeat Password:', validators=[InputRequired(message='Password Required'),
                                                                EqualTo('password', message='Passwords must match')])
    create_user = SubmitField('Sign up!')


class LoginForm(FlaskForm):

    username = StringField('Username: ',
                           validators=[InputRequired(message='username required')])
    password = PasswordField('Password: ',
                             validators=[InputRequired(message='password required')])
    login_button = SubmitField('Login')
