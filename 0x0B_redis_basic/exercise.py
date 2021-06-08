#!/usr/bin/env python3
""" [Module that holds writing strings to Redis]
"""

import redis
from uuid import uuid4
from typing import Union


class Cache:
    """ Cache class
    """

    def __init__(self):
        """ Constructor method,
            store an instance of the
            Redis client as a private variable
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that generates a random key and stores
            the input data also takes an argument (data)
            and returns a string
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
