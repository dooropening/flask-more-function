import os
from pymongo import MongoClient


# mongodb_uri = os.environ.get('MONGODB_URI')
# client = MongoClient(mongodb_uri)

client = MongoClient("localhost", 27017)
db = client.ai4o_db
collection = db.ai4o_collection

