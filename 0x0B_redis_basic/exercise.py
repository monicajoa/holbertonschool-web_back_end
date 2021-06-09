#!/usr/bin/env python3
""" [Module that holds writing strings to Redis]
"""

import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ (Incrementing values),
        decorator that takes a single method
        Callable argument and returns a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Method that contains a wrapped function,
            which allows access to the Redis instance
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that generates a random key and stores
            the input data also takes an argument (data)
            and returns a string
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float]:
        """ (Reading from Redis and recovering original type),
            Method that takes one argument(key) and one optional
            argument(fn), this callable converts the data to the
            desired format
        """
        new_value = self._redis.get(key)
        if fn:
            return (fn(new_value))
        else:
            return new_value

    def get_str(self, key: str) -> str:
        """ Method that will parameterize (Cache.get)
            with correct conversion function
        """
        new_value = self._redis.get(key)
        decode_value = new_value.decode("utf-8")
        return decode_value

    def get_int(self, key: str) -> int:
        """ Method that will parameterize (Cache.get)
            with correct conversion function
        """
        new_value = self._redis.get(key)
        return int(new_value)
