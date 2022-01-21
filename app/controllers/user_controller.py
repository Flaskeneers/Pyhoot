from app.persistence.repository import user_repo


def update_by_username(username, new_data):
    return user_repo.update_by_username(username, new_data)

