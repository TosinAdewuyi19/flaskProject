from bson.objectid import ObjectId
from src.app import mongo

class BidderRepository:
    def __init__(self):
        self.collection = mongo.db.bidders

    def insert_bidder(self, bidder_data):
        result = self.collection.insert_one(bidder_data)
        bidder_data["_id"] = str(result.inserted_id)
        return bidder_data

    def find_by_email(self, email):
        bidder = self.collection.find_one({"email": email})
        if bidder:
            bidder["_id"] = str(bidder["_id"])
        return bidder

    def find_by_id(self, bidder_id):
        try:
            bidder = self.collection.find_one({"_id": ObjectId(bidder_id)})
            if bidder:
                bidder["_id"] = str(bidder["_id"])
            return bidder
        except Exception:
            return None
