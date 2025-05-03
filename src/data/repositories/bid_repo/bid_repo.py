from flask_pymongo import PyMongo

class BidRepository:
    def __init__(self, mongo: PyMongo):
        self.mongo = mongo

    def create_bid(self, bid_data):
        self.mongo.db.bids.insert_one(bid_data)

    def find_bids_by_auction(self, auction_id):
        return self.mongo.db.bids.find({'auction_id': auction_id})
