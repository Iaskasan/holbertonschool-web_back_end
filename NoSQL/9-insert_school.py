#!/usr/bin/env python3
'''insert new docs in the collection'''


def insert_school(mongo_collection, **kwargs):
    '''insert new docs in the collection
    based on args passed to the function'''
    if mongo_collection is None:
        return None
    mongo_collection.insert(kwargs).inserted_id
    return mongo_collection
