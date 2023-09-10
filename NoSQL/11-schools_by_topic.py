#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
        mongo_collection: object pymongo
        topic: (string)will be topic searched
    """
    topc = {"topics": topic}
    docs = mongo_collection.find(topc)

    return list(docs)
