#!/usr/bin/env python3
'''return a list of string containing a specified topic'''


def schools_by_topic(mongo_collection, topic):
    '''return a list of string with a specified topic'''
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
