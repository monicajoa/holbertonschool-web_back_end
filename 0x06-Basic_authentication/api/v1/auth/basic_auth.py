#!/usr/bin/env python3
"""[Basic auth]
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """[Class that inherits from Auth]

    Args:
        Auth ([Class]): [Parent class]
    """

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """ Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header[:6] == 'Basic ':
            return None
        else:
            return authorization_header[6:]
