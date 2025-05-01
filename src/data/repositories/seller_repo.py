from bson.objectid import ObjectId
from src.extensions import mongo

class SellerRepository:
    def __init__(self):
        pass

    def find_all(self):
        return list(mongo.db.sellers.find())

    def insert_seller(self, seller_data):
        return mongo.db.sellers.insert_one(seller_data)

    def find_by_email(self, email):
        return mongo.db.sellers.find_one({"email": email})

    def find_by_id(self, seller_id):
        return mongo.db.sellers.find_one({"_id": seller_id})

    def update_one(self, seller_id, update_data):
        return mongo.db.sellers.update_one({"_id": seller_id}, {"$set": update_data})

    def delete_one(self, seller_id):
        return mongo.db.sellers.delete_one({"_id": seller_id})