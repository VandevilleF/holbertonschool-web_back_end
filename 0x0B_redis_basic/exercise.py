#!/usr/bin/env python3
""" Cache class module
"""
import uuid
import redis
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator that count
    how many times methods of the Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Increments the count every time the method is called
        Returns
        - the value returned by the original method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache():
    """ Cache class
    """
    def __init__(self):
        """ Initialize the Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method, generate a random key,
        store the input data in Redis using the random key
        Returns
          - the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """ Retrieve data from Redis
        and optionally apply a conversion function.
        """
        value = self._redis.get(key)
        if value is None:
            return None

        if fn:
            return fn(value)

        return value

    def get_str(self, key: str) -> str:
        """ Retrieve a string value from Redis.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Retrieve an integer value from Redis.
        """
        return self.get(key, fn=int)
