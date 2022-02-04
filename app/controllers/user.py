from app.persistence.repository import user_repo as repo


def create_user(email: str, username: str, password: str):
    return repo.create_user(email, username, password)


def get_by_username(username: str):
    return repo.get_by_username(username)


def get_by_email(email: str):
    return repo.get_by_email(email)


def check_existing_users(username: str, email: str):
    return repo.check_existing_users(username, email)


def verify_password(user, password):
    return repo.verify_password(user.password, password)


def get_all_users():
    return repo.get_all_users()


def update_by_username(username, new_data):
    return repo.update_by_username(username, new_data)

