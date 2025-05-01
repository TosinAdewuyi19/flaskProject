from src.data.models.validator import Validator

class ListingsDTO:
    def __init__(self, title, description, starting_price, seller_id):
        self.title = title
        self.description = description
        self.starting_price = starting_price
        self.seller_id = seller_id

    @classmethod
    def from_dict(cls, data):
        if not all(k in data for k in ("title", "description", "starting_price", "seller_id")):
            raise ValueError("Missing required fields for product")
        Validator.validate_required_fields(data, ["name", "email", "password"])
        if not Validator.is_email_valid(data["email"]):
            raise ValueError("Invalid email format")
        return cls(
            title=data["title"],
            description=data["description"],
            starting_price=float(data["starting_price"]),
            seller_id=data["seller_id"]
        )

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "starting_price": self.starting_price,
            "seller_id": self.seller_id
        }
