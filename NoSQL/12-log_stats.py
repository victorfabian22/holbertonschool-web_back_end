#!/usr/bin/env python3
"""Task 12:
    Log stats"""
from pymongo import MongoClient
import pprint

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    logs = 0
    gets = 0
    posts = 0
    puts = 0
    patchs = 0
    deletes = 0
    status = 0
    for doc in nginx_collection.find():
        logs += 1
        for key, value in doc.items():
            if value == "POST":
                posts += 1
            elif value == "GET":
                gets += 1
            elif value == "PUT":
                puts += 1
            elif value == "PATCH":
                patchs += 1
            elif value == "DELETE":
                deletes += 1
            elif value == "/status":
                status += 1
    print(f"{logs} logs\nMethods:")
    print(f"\tmethod GET: {gets}")
    print(f"\tmethod POST: {posts}")
    print(f"\tmethod PUT: {puts}")
    print(f"\tmethod PATCH: {patchs}")
    print(f"\tmethod DELETE: {deletes}")
    print(f"{status} status check")
