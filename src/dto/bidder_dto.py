from src.data.models.validator import Validator

class BidderDTO:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, data):
        if not all(v in data for v in ("name", "email", "password")):
            raise ValueError("Missing required fields for bidder")
        Validator.validate_required_fields(data, ["name", "email", "password"])
        if not Validator.is_email_valid(data["email"]):
            raise ValueError("Invalid email format")
        return cls(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
