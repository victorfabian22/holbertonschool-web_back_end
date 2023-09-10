#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Args:
        mongo_collection: object pymongo
        name: (string) the school name to update
        topics: (list of strings) list of topics
    """
    filtro = {"name": name}
    valor = {"$set": {"topics": topics}}
    mongo_collection.update_many(filtro, valor)
