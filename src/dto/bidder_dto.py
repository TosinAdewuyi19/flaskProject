class BidderDTO:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, data):
        if not all(k in data for k in ("name", "email", "password")):
            raise ValueError("Missing required fields for bidder")
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
