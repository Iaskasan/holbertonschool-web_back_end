#!/usr/bin/env python3
'''Update topics of a school document in the MongoDB collection'''


def update_topics(mongo_collection, name, topics):
    '''update topics of a specified document'''
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
