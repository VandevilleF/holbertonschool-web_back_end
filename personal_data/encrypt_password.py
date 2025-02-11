#!/usr/bin/env python3
"""encrypt_password module"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password,
    which is a byte string."""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate that the provided password
    matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
