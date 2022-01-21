from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms.validators import DataRequired


# TODO: change DataRequired() to InputRequired()
class BaseQuestionForm(FlaskForm):
    description = wtf.StringField("Description", validators=[DataRequired()])
    correct_answer = wtf.StringField("Correct Answer", validators=[DataRequired()])
    wrong_answers = wtf.FieldList(wtf.StringField(validators=[DataRequired()]),
                                  min_entries=3, max_entries=3)


class CreateQuestionForm(BaseQuestionForm):
    submit = wtf.SubmitField("Create Question")


class EditQuestionForm(BaseQuestionForm):
    submit = wtf.SubmitField("Edit Question")
