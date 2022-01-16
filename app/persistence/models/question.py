from pymongo.collection import Collection


from .base import Document
from ..db import db


class Question(Document):
    collection: Collection = db.questions
