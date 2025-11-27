from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)

db = client["mock_payment_db"]

users_collection = db["users"]
payments_collection = db["payments"]
