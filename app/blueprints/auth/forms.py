from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Length, InputRequired, Email, EqualTo, DataRequired


class SignupForm(FlaskForm):

    email = StringField('E-mail: ', validators=[DataRequired(message='Please enter a valid Email!!'),
                                                Email(message='Please enter a valid Email')])

    username = StringField('Username: ', validators=[DataRequired(message='This is required'), Length(3, 25)])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(3, 30)])
    repeat_pass = PasswordField('Repeat Password:', validators=[DataRequired(), EqualTo('password')])

    create_user = SubmitField('Sign up!')


class LoginForm(FlaskForm):

    username = StringField('Username: ', validators=[InputRequired()])
    password = PasswordField('Password: ', validators=[InputRequired()])

    login_button = SubmitField('Login')

class EditUser(FlaskForm):

    email = StringField('E-mail: ', validators=[DataRequired(),Email()])
    old_password:   PasswordField()
    new_password:   PasswordField('New Password: ', validators=[DataRequired(), Length(3, 30)])
