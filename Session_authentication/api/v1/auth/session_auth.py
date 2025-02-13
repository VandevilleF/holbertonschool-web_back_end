#!/usr/bin/env python3
"""
SessionAuth module
"""
from api.v1.auth.auth import Auth
from api.v1.views.users import User
import uuid


class SessionAuth(Auth):
    """ SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return:
        - a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Return:
        - a User instance based on a cookie value
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)

        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        print("User ID trouvé:", user_id)

        if user_id is None:
            return None

        user = User.get(user_id)
        print("Utilisateur trouvé:", user)

        return user
