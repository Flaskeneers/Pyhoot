from .. import bp_user


@bp_user.get("/quizzes")
def create_quiz_get():
    pass


@bp_user.post("/quizzes")
def create_quiz_post():
    pass


@bp_user.get("/quizzes/detail/<quiz_id>")
def detail_quiz_get():
    pass


@bp_user.get("/quizzes/edit/<quiz_id>")
def edit_quiz_get():
    pass


@bp_user.put("/quizzes/edit/<quiz_id>")
def edit_quiz_post():
    pass


@bp_user.delete("/quizzes/delete/<quiz_id>")
def delete_quiz():
    pass
