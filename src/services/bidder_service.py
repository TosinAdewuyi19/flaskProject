from src.repositories.bidder_repo import BidderRepository
from src.exceptions.custom_exceptions import BadRequestError

class BidderService:
    def __init__(self):
        self.bidder_repo = BidderRepository()

    def register_bidder(self, bidder_dto):
        existing = self.bidder_repo.find_by_email(bidder_dto.email)
        if existing:
            raise BadRequestError("Bidder already exists with this email")
        bidder_data = bidder_dto.to_dict()
        return self.bidder_repo.insert_bidder(bidder_data)

    def get_bidder_by_id(self, bidder_id):
        return self.bidder_repo.find_by_id(bidder_id)
