from dataclasses import dataclass
from random import shuffle


@dataclass
class Question:
    description: str
    correct_answer: str
    wrong_answers: list[str]

    @property
    def choices(self, rearrange: bool = True) -> list[str]:
        answers = [self.correct_answer] + self.wrong_answers
        if rearrange:
            shuffle(answers)
        return answers


@dataclass
class Quiz:
    id: str
    created_by: str
    title: str
    questions: list[Question] | None = None
