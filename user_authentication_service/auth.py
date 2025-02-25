#!/usr/bin/env python3
""" Auth module
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Returns bytes
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """Return a string representation of a new UUID
    """
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """ Find the user corresponding to the email,
        generate a new UUID and store it in the db as the user s session_id,
        then return the session ID."""
        try:
            current_user = self._db.find_user_by(email=email)
            current_user.session_id = _generate_uuid()

            return current_user.session_id

        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: bytes) -> User:
        """ Returns the corresponding User or None.
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """ Updates the corresponding user s session ID to None.
        """
        user = self._db.find_user_by(user_id=user_id)
        user.session_id = None

        self._db.commit()

        return None
