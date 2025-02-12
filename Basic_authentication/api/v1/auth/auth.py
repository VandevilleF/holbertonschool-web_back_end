#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Authentication template class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return:
            - False or True if the path is not in the list of strings
        """
        if path is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ Return:
            - None
            """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return:
            - None
        """
        return None
