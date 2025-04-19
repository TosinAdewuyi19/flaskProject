from flask import db
from models.auction import Auction

class AuctionServices:
    def create_auction(self, item_name, starting_bid, end_bid, end_time):
        auction = Auction(item_name, starting_bid, end_time,)
        db.auctions.insert(auction.to_dict())
        return auction

    def get_auction(self):
        return list(db.auctions.find({},{"_id": 0}))
