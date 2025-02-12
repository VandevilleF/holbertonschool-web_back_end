#!/usr/bin/env python3
"""
Basic_auth module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Return:
        - the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None

        if authorization_header.startswith('Basic '):
            return authorization_header.partition('Basic ')[2]

        return None
