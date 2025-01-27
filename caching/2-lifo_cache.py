#!/usr/bin/python3
"""FIFOCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Child class inherit of class BaseCaching that defines:

    - constants of your caching system
    - where your data are stored (in a dictionary)"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item in the cache with FIFO algorithm"""
        if (key is None or item is None):
            return
        if (
            key not in self.cache_data and
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
        ):
            print("DISCARD: {}".format(self.last_key))
            del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Get an item by key"""
        if (key is None or self.cache_data.get(key) is None):
            return
        else:
            return self.cache_data[key]
