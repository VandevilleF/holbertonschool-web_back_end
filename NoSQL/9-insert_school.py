#!/usr/bin/env python3
"""Inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
# The insert_one() method returns a InsertOneResult object
# which has a property, inserted_id
# that holds the id of the inserted document.
