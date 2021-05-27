#!/usr/bin/env python3
""" [Module that holds Auth]
"""

import bcrypt


def _hash_password(password: str) -> str:
    """ Method Hash password, that takes in a password
        string argumentsand, Returns bytes
    """
    sal = bcrypt.gensalt()
    password = password.encode()
    return bcrypt.hashpw(password, sal)
