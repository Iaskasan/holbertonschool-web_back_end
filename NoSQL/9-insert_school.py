#!/usr/bin/env python3
'''insert new docs in the collection'''


def insert_school(mongo_collection, **kwargs):
    '''insert new docs in the collection
    based on args passed to the function'''
    mongo_collection.insert(**kwargs)
