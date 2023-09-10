#!/usr/bin/env python3
"""Function that inserts a document into a collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Args:
       mongo_collection: pymongo object
       **kwargs: arguments dictionary
    """
    # **kwargs(documento para agregar a coleccion)
    d_id = mongo_collection.insert_one(kwargs).inserted_id
    return d_id
