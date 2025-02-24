#!/usr/bin/env python3
""" Auth module
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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
        try:
            current_user = self._db.find_user_by(email=email)
            if current_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            user_pwd = _hash_password(password)
            user = self._db.add_user(email, user_pwd)

            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ Retrieve user if exist and check if password match,
        Return True if password match else False"""
        try:
            current_user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'),
                           current_user.hashed_password)
        except NoResultFound:
            return False
