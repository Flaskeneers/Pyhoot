from pymongo.collection import Collection

from .base import Document
from ..db import db


class Lobby(Document):
    collection: Collection = db.lobbies

    # attributes
    # - quiz: Quiz
    # - players: list[Player] or list[User]
    #   - user: User
    #   - score: int
