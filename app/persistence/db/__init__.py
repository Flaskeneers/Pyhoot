from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database

load_dotenv()

PROTOCOL = getenv("MONGO_DB_PROTOCOL")
USER = getenv("MONGO_DB_USER")
PASS = getenv("MONGO_DB_PASS")
HOST = getenv("MONGO_DB_HOST")
PORT = getenv("MONGO_DB_PORT")
DB_NAME = getenv("MONGO_DB_NAME")

DEFAULT_DB_URI = f"{PROTOCOL}://{USER}:{PASS}@{HOST}:{PORT}"

client: MongoClient = MongoClient(DEFAULT_DB_URI, authSource="admin")
db: Database = client[f"{DB_NAME}-test"]


def init_mongodb(uri: str, name: str) -> None:
    global client, db

    client = MongoClient(uri, authSource="admin")
    db = client[name]


def drop_database(name: str) -> None:
    client.drop_database(name)
