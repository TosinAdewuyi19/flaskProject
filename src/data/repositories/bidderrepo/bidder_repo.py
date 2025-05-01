from src.extensions import mongo

class BidderRepository:
    def __init__(self):
        pass

    def place_bid(self, bid_data):
        return mongo.db.bids.insert_one(bid_data)

    def find_bids_by_id(self, bidder_id):
        return list(mongo.db.bids.find({"bidder_id": bidder_id}))

    def find_bids_by_email(self, bidder_email):
        return list(mongo.db.bids.find({"email": bidder_email}))

    def insert_bidder(self, bid_data):
        return mongo.db.bids.insert_one(bid_data)

    def save_bid(self, bid_data):
        return mongo.db.bids.update({"_id": bid_data["_id"]}, bid_data)



