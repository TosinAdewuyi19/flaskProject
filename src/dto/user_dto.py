from src.data.models.usertype import UserType
from src.data.models.validator import Validator

class UserDTO:
    def __init__(self, data):
        Validator.validate_required_fields(data, ["name", "email", "password", "user_type"])
        if data["user_type"] not in UserType.list():
            raise ValueError("Invalid user type")
        if not Validator.is_email_valid(data["email"]):
            raise ValueError("Invalid email format")

        self.name = data["name"]
        self.email = data["email"]
        self.password = data["password"]
        self.user_type = data["user_type"]

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "user_type": self.user_type
        }
