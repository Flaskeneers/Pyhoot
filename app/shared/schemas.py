from dataclasses import dataclass


@dataclass
class Question:
    description: str
    correct_answer: str
    wrong_answers: list[str]


@dataclass
class Quiz:
    id: str
    created_by: str
    title: str
    questions: list[Question] | None = None
