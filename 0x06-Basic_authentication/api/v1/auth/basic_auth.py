#!/usr/bin/env python3
"""[Basic auth]
"""

from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of a Base64
        string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return decode
        except Exception:
            return None
        else:
            return None
