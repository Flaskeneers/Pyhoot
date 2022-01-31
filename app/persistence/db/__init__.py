from pymongo import MongoClient
from pymongo.database import Database

client: MongoClient | None = None
db: Database | None = None


def init_mongodb(uri: str, name: str) -> None:
    global client, db

    client = MongoClient(uri, authSource="admin")
    db = client[name]


def drop_database(name: str) -> None:
    client.drop_database(name)
