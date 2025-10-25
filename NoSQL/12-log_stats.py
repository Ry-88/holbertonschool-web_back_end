#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
Database: logs
Collection: nginx
"""

from pymongo import MongoClient


def main():
    """Main function to display Nginx logs stats."""
    # Connect to MongoDB (default localhost:27017)
    client = MongoClient("mongodb://localhost:27017/")

    # Access database and collection
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod={method} count={count}")

    # Logs with method=GET and path=/status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
