from bson.objectid import ObjectId
from src.app import mongo

class SellerRepository:
    def __init__(self):
        self.collection = mongo.db.sellers

    def insert_seller(self, seller_data):
        result = self.collection.insert_one(seller_data)
        seller_data["_id"] = str(result.inserted_id)
        return seller_data

    def find_by_email(self, email):
        seller = self.collection.find_one({"email": email})
        if seller:
            seller["_id"] = str(seller["_id"])
        return seller

    def find_by_id(self, seller_id):
        try:
            seller = self.collection.find_one({"_id": ObjectId(seller_id)})
            if seller:
                seller["_id"] = str(seller["_id"])
            return seller
        except Exception:
            return None
