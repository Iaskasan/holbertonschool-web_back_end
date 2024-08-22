#!/usr/bin/env python3
'''Salut Lucas'''
from pymongo import MongoClient


def list_all(mongo_collection):
    '''au revoir benoit'''
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
