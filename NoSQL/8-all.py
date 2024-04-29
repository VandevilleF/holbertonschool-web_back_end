#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    doc_collec = []
    for doc in mongo_collection.find():
        doc_collec.append(doc)
    return doc_collec
