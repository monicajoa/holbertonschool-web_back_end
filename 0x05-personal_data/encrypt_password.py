#!/usr/bin/env python3
"""[This module contains encryption passwords]
"""

import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """[Function that expects one string argument]

    Args:
        password (str)

    Returns:
        bytes: [Hashed password, which is a byte string]
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
