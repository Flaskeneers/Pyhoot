from flask import render_template, request, jsonify, make_response
from flask_login import login_required, current_user

from .. import bp_user

current_question = 0
dummyQuiz = [{
    "game_id": "temp",
    "quiz_id": "temp",
    "quiz_title": "DummyQuiz",
    "quiz_progress": f"{current_question + 1} out of 10",

    "description": "What is 2 + 2?",
    "choices": ["1", "2", "3", "4"]

},
    {
        "game_id": "temp",
        "quiz_id": "temp",
        "quiz_title": "DummyQuiz",
        "quiz_progress": f"{current_question +1} out of 2",

        "description": "What is 2 + 3?",
        "choices": ["5", "2", "3", "4"]

    }
]


@bp_user.route('/test')
@login_required
def hello_world():
    return render_template('user/chat.html', username=current_user.username)


@bp_user.route("/play")
def play():
    return render_template("user/play.html", data=dummyQuiz[current_question])


@bp_user.route("/play/next", methods=["POST"])
def update_question():
    correct_answer = 2
    request_ = request.get_json()
    print(request_)

    response_ = make_response(jsonify(correct_answer))

    return response_
