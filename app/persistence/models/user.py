from pymongo.collection import Collection

from .base import Document
from ..db import db


class User(Document):
    collection: Collection = db.users

