from src.data.repositories.listings_repo import ProductRepository
from src.exceptions.custom_exceptions import BadRequestError

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepository()

    def create_product(self, product_dto):
        product_data = product_dto.to_dict()
        return self.product_repo.insert_product(product_data)

    def get_all_products(self):
        return self.product_repo.find_all()
