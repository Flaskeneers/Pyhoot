from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms.validators import DataRequired


class AnswerForm(wtf.Form):
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
    submit = wtf.SubmitField("Edit Question")
