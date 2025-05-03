class BidService:
    def __init__(self):
        self.bids = []

def place_bid(self, bid_data):
    if not bid_data or 'amount' not in bid_data or 'auction_id' not in bid_data or 'bidder' not in bid_data:
        raise ValueError("Bid data must include 'amount', 'auction_id', and 'bidder'.")

    bid_id = len(self.bids) + 1
    bid = {
        "id": bid_id,
        "amount": bid_data['amount'],
        "auction_id": bid_data['auction_id'],
        "bidder": bid_data['bidder']
    }
    self.bids.append(bid)
    print("Bid created:", bid)
    return bid

def get_bids_by_auction(self, auction_id):
    auction_bids = [bid for bid in self.bids if bid['auction_id'] == auction_id]
    return auction_bids

def delete_bid(self, bid_id):

        for bid in self.bids:
            if bid['id'] == bid_id:
                self.bids.remove(bid)
                print("Bid deleted:", bid)
                return bid
        raise ValueError("Bid not found.")

bid_service = BidService()
