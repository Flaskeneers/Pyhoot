from bson import ObjectId
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

from app.persistence.models.user import User
from app.shared.resultlist import ResultList


def create_user(email: str, username: str, password: str) -> [list]:
    """Creates a user in database, if validation from Check_existing_users passes"""

    data = dict(
        email=email,
        username=username,
        password=generate_password_hash(password),
        is_admin=False,
        is_active=True)

    if check_existing_users(username, email):
        user = User(data)
        user.save()
        print(f'Created user {username}')
        return user


def get_all_users():
    return ResultList(User(i) for i in User.collection.find())


def get_by_username(username: str):
    return ResultList(User(i) for i in User.collection.find(dict(username=username))).first_or_none()


def delete_user(username):
    pass


def update_user(username, update):
    pass


def check_existing_users(username: str, email: str) -> bool:
    """ Returns True if Email or username doesn't exist in the database"""

    if User.collection.find_one({"username": username}) is not None:
        print(f"{username} already exists in database")
        return False

    if User.collection.find_one({"email": email}) is not None:
        print(f"{email} already exists in database")
        return False
    return True


def verify_password(username: str, password: str) -> bool:
    """ Compares entered credentials with credentials in DB."""

    hashed = User.collection.find_one({'username': username},
                                      {'password': 1, '_id': False}).get('password')
    return check_password_hash(hashed, password)
