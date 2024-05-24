from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def connect_to_mongodb(host="localhost", port=27017, db_name="ai4o_db", username=None, password=None):
    try:
        if username and password:
            client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
        else:
            client = MongoClient(host, port)

        db = client[db_name]
        return db
    except ConnectionFailure:
        print("Failed to connect to MongoDB server.")
        return None


# 导出db对象
db = connect_to_mongodb()
