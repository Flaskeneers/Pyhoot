from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms.validators import DataRequired


# region Profile

class EditProfileForm(FlaskForm):
    pass


# endregion profile


# region Question

class AnswerForm(FlaskForm):
    text = wtf.StringField("", validators=[DataRequired()])


class BaseQuestionForm(FlaskForm):
    description = wtf.StringField("Description",
                                  validators=[DataRequired()])
    correct_answer = wtf.FormField(AnswerForm)
    wrong_answers = wtf.FieldList(wtf.FormField(AnswerForm),
                                  min_entries=3, max_entries=3)


class CreateQuestionForm(BaseQuestionForm):
    submit = wtf.SubmitField("Create Question")


class EditQuestionForm(BaseQuestionForm):
    submit = wtf.SubmitField("Update Question")


# endregion Question


# region Quiz

class CreateQuizForm(FlaskForm):
    pass


class EditQuizForm(FlaskForm):
    pass

# endregion Quiz
