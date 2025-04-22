from src.data.models.validator import Validator

class SellerDTO:
    def __init__(self, name, email, store_name, password):
        self.name = name
        self.email = email
        self.store_name = store_name
        self.password = password

    @classmethod
    def from_dict(cls, data):
        if not all(k in data for k in ("name", "email", "store_name", "password")):
            raise ValueError("Missing required fields for seller")
        Validator.validate_required_fields(data, ["name", "email", "password"])
        if not Validator.is_email_valid(data["email"]):
            raise ValueError("Invalid email format")
        return cls(
            name=data["name"],
            email=data["email"],
            store_name=data["store_name"],
            password=data["password"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "store_name": self.store_name,
            "password": self.password
        }
