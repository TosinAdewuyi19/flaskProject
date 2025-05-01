from src.data.models.bid import Bid
from src.data.models.bidders import Bidder
from src.data.repositories.bidderrepo.bidder_repo import BidderRepository
from werkzeug.security import generate_password_hash

class BidderService:
    def __init__(self):
        self.bidder_repo = BidderRepository()

    def register_bidder(self, data):
        required_fields = ['username', 'email', 'password']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} is required")

            hashed_password = generate_password_hash(data['password'])
            bidder = Bidder(
                username=data['username'],
                email=data['email'],
                password=hashed_password,
                user_type="bidder"
            )
            self.bidder_repo.save_bid(bidder.to_dict())

        # existing = self.bidder_repo.find_bids_by_email(bidder_dto.email)
        # if existing:
        #     raise BadRequestError("Bidder already exists with this email")
        # bidder_data = bidder_dto.to_dict()
        # return self.bidder_repo.insert_bidder(bidder_data)

    def get_bidder_by_id(self, bidder_id):
        return self.bidder_repo.find_bids_by_id(bidder_id)

    def place_bid(self, bidder_id, product_id, amount):
        if amount <= 0:
            raise ValueError("Bid amount must be positive")

        bid = Bid(bidder_id, product_id, amount)
        return self.bidder_repo.place_bid(bid.to_dict())
