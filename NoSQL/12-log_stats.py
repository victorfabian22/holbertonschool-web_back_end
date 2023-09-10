#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost')
    db = client["logs"]
    var = db["nginx"]

    print(f"{var.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print(f"\tmethod {m}: {var.count_documents({'method': m})}")

    mesage = "status check"

    print(f"{var.count_documents({'method': 'GET', 'path': '/status'})} {mesage}")
