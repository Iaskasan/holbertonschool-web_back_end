#!/usr/bin/env python3
'''insert new docs in the collection'''


def insert_school(mongo_collection, **kwargs):
    '''insert new docs in the collection
    based on args passed to the function'''
    result = mongo_collection.insert(kwargs)
    return result.inserted_id
