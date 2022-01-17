from bson import ObjectId

from werkzeug.security import generate_password_hash

from app.persistence.models.user import User
from app.shared.resultlist import ResultList


def create_user(email: str, username: str, password: str) -> [list]:

    data = dict(
        email=email,
        username=username,
        password=generate_password_hash(password),
        is_admin=False,
        is_active=True)

    user = User(data)
    user.save()
    print(user)
    return user


def get_all_users():
    return ResultList(User(i) for i in User.collection.find())


def get_by_username(username: str):
    return ResultList(User(i) for i in
                      User.collection.find(dict(username=username))).first_or_none()


def delete_user(username):
    pass


def update_user(username, update):
    pass
