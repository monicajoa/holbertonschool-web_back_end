#!/usr/bin/env python3
""" [Module that holds Auth]
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Method Hash password, that takes in a password
        string argumentsand, Returns bytes
    """
    sal = bcrypt.gensalt()
    password = password.encode()
    return bcrypt.hashpw(password, sal)


def _generate_uuid() -> str:
    """ Method Generate UUIDs, using the uuid module,
        Return a string representation of a new UUID
    """
    new_uuid = str(uuid4())
    return new_uuid


class Auth:
    """ Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method Register user, that takes email and password arguments,
            Return a User object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            register_user = self._db.add_user(email, hashed_password)
            return register_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Method Credentials validation, Try to reach the user by email,
            It should expect required arguments by email and password and
            Return a boolean
        """
        try:
            find_user = self._db.find_user_by(email=email)
            password = password.encode()
            valid_login = bcrypt.checkpw(password, find_user.hashed_password)
            return valid_login
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Method Get session ID, it takes an email string argument,
            find the user corresponding to the email, generate a new UUID
            and save it to the database as the user's session_id,
            Return the session ID
        """
        try:
            find_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        self._db.update_user(find_user.id, session_id=_generate_uuid())
        return find_user.session_id