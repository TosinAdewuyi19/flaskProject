from src.data.repositories.seller_repo import SellerRepository
from src.exceptions.custom_exceptions import BadRequestError

class SellerService:
    def __init__(self):
        self.seller_repo = SellerRepository()

    def register_seller(self, seller_dto):
        existing = self.seller_repo.find_by_email(seller_dto.email)
        if existing:
            raise BadRequestError("Seller already exists with this email")
        seller_data = seller_dto.to_dict()
        return self.seller_repo.insert_seller(seller_data)

    def get_seller_by_id(self, seller_id):
        return self.seller_repo.find_by_id(seller_id)
