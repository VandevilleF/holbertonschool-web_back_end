#!/usr/bin/env python3
"""
Basic_auth module
"""

from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """ Return:
        - the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            decode = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return decode

        except (TypeError, ValueError):
            return None
