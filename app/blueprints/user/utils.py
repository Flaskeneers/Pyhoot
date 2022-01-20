def get_clean_question_form_data(form_data: dict) -> dict:
    return dict(
        description=form_data["description"],
        correct_answer=form_data["correct_answer"]["text"],
        wrong_answers=[wrong_answer["text"] for wrong_answer
                       in form_data["wrong_answers"]]
    )


def is_request_args_valid(*args) -> bool:
    for arg in args:
        if not arg:
            return False
    return True
