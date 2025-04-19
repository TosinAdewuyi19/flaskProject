class Auction:
    def __init__(self, item_name, starting_bid, end_time):
        self.item_name = item_name
        self.starting_bid = starting_bid
        self.end_time = end_time
        self.bids = []

    def add_item_to_dict(self):
        return {
            'item_name': self.item_name,
            'starting_bid': self.starting_bid,
            'end_time': self.end_time,
            'bids': self.bids
        }