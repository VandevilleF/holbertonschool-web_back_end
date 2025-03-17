#!/usr/bin/env python3
""" Cache class module
"""
import uuid
import redis


class Cache():
    """ Cache class
    """
    def __init__(self):
        """ Initialize of class Cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """ Store method, generate a random key,
        store the input data in Redis using the random key
        Returns
          - the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
