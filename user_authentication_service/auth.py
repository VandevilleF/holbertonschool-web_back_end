#!/usr/bin/env python3
""" Auth module
"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Returns bytes
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize a new DB instance
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Save the user in DB and return a User object
        """
        if self._db._session.query(User).filter_by(email=email).first():
            raise ValueError(f"User {email} already exists")

        user_pwd = _hash_password(password)
        user = self._db.add_user(email, user_pwd)

        return user
