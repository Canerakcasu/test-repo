from dataclasses import dataclass
from typing import List


@dataclass
class User:
    id: int
    username: str
    email: str


def get_users_by_id(user_ids: List[int]) -> List[User]:
    """Return a list of users matching the provided IDs."""
    if not user_ids:
        return []

    sanitized_ids = [int(user_id) for user_id in user_ids if user_id is not None]
    if not sanitized_ids:
        return []

    users = [
        User(id=1, username="alice", email="alice@example.com"),
        User(id=2, username="bob", email="bob@example.com"),
    ]
    return [user for user in users if user.id in sanitized_ids]
