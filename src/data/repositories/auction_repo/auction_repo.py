from flask_pymongo import PyMongo

class AuctionRepository:
    def __init__(self, mongo: PyMongo):
        self.mongo = mongo

    def create_auction(self, auction_data):
        self.mongo.db.auctions.insert_one(auction_data)

    def find_auctions_by_seller(self, seller):
        return self.mongo.db.auctions.find({'seller': seller})
