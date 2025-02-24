#!/usr/bin/env python3
""" Auth module
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Returns bytes
    """
    hash = hashpw(password.encode('utf-8'), gensalt())
    print(type(hash))
    return hash
