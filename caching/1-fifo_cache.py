#!/usr/bin/python3
"""FIFOCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Child class inherit of class BaseCaching that defines:

    - constants of your caching system
    - where your data are stored (in a dictionary)"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache with FIFO algorithm"""
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            self.cache_data.pop(next(iter(self.cache_data)))

    def get(self, key):
        """Get an item by key"""
        if (key is None or self.cache_data.get(key) is None):
            return
        else:
            return self.cache_data[key]
