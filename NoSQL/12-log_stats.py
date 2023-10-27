#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    col = db['nginx']
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{col.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        print(f"\tmethod {method}: {col.count_documents({'method': method})}")

    sc = "status check"
    check = col.count_documents({'method': 'GET','path': '/status'})
    print(f"{check} {sc}")
