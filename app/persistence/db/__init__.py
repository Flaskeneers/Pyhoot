from pymongo import MongoClient

client = None
db = None


def init_mongodb(uri: str, name: str) -> None:
    global client, db

    client = MongoClient(uri, authSource="admin")
    db = client[name]
