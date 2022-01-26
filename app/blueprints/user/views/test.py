from flask import render_template, url_for
from flask_login import login_required, current_user

from .. import bp_user

dummyQuiz = [{
    "quiz_id": "quizID",
    "question": "What is 2 + 2?",
    "answers": [2, 1, 3, 4],
    "correct_answer": 3,
    "current_question": 0

}, {
       "quiz_id": "quizID",
       "question": "What's the capital of Sweden?",
       "answers": ["Gothenburg", "Stockholm", "Malmö", "Oslo"],
       "correct_answer": "Stockholm",
       "current_question": 1
   }
]

@ bp_user.route('/test')
@ login_required
def hello_world():
    return render_template('user/chat.html', username=current_user.username)


@bp_user.route("/play")
def play():
    return render_template("user/play.html", quiz=dummyQuiz)
