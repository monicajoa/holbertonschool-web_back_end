#!/usr/bin/env python3
"""[Module that holds auth class]
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """[Class to manage the API authentication]
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[Public method]

        Args:
            path (str)
            excluded_paths (List[str])

        Returns:
            bool: [False]
        """
        return False

    def authorization_header(self, request=None) -> str:
        """[Public method]

        Args:
            request ([type], optional): Defaults to None

        Returns:
            str: [None]
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[Public method]

        Returns:
            [type]: [None]
        """
        return None
