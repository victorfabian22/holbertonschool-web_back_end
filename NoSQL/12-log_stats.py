#!/usr/bin/env python3
"""script that provides some stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost')
    Database = client["logs"]
    col = Database["nginx"]

    print(f"{col.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print(f"\tmethod {method}: {col.count_documents({'method': method})}")

    mns = "status check"
    print(f"{col.count_documents({'method': 'GET','path': '/status'})} {mns}")
