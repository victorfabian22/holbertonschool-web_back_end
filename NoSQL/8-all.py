#!/usr/bin/env python3
"""List all documents in Python"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """function that lists all documents in a collection"""
    # list_all(mongodb://127.0.0.1:27017.my_db.school)
    results = []

    for r in mongo_collection.find():
        results.append(r)

    return results
