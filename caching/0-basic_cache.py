#!/usr/bin/python3
"""BasicCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Child class inherit of class BaseCaching that defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)"""
    def __init__(self):
        """Initiliaze"""
        BaseCaching.__init__(self)
    def put(self, key, item):
        """Add an item in the cache"""
        if (key == None or item == None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if (key == None or self.cache_data.get(key) == None):
            return
        else:
            return self.cache_data[key]

