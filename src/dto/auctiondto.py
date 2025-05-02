class AuctionDTO:
    def __init__(self, title, description, starting_bid, current_bid, end_time, highest_bidder=None):
        self.title = title
        self.description = description
        self.starting_bid = starting_bid
        self.current_bid = current_bid
        self.end_time = end_time
        self.highest_bidder = highest_bidder  # Store highest bidder's username
        self.image_url = None  # Optional: You can set this later
