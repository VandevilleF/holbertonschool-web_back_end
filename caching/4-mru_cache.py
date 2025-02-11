#!/usr/bin/python3
"""FIFOCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Child class inherit of class BaseCaching that defines:

    - constants of your caching system
    - where your data are stored (in a dictionary)"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if (key is None or item is None):
            return

        if key in self.cache_data:
            self.access_order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.access_order.pop()
            print("DISCARD: {}".format(mru_key))
            del self.cache_data[mru_key]

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return

        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
