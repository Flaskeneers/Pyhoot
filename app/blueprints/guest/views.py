from flask import redirect, render_template, url_for

from . import bp_guest
from app.persistence.repository import question_repo


@bp_guest.get("/")
def index():
    return render_template("guest/index.html")


@bp_guest.get("/question")
def create_question():
    question = question_repo.create(description="What is 2 + 2?",
                                    correct_answer="4",
                                    wrong_answers=["1", "2", "3"])
    print(question)
    return redirect(url_for(".index"))


@bp_guest.get("/test-update")
def test_update():
    all_questions = question_repo.get_all()
    some_id = all_questions[0].id
    if question_repo:
        question = question_repo.get_by_id(some_id)
        question.update_with({"description": "What is 2 + 3?",
                              "correct_answer": "5"})
    return redirect(url_for(".index"))


@bp_guest.get("/test-delete")
def delete_all_questions():
    documents_deleted = question_repo.delete_all()
    print(f"Docs deleted: {documents_deleted}")
    return redirect(url_for(".index"))
