class Bidder:
    def __init__(self, email, username, password, user_type="bidder"):
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type

    def to_dict(self):
        data = {
            "name": self.username,
            "email": self.email,
            "password": self.password,
            "user_type": self.user_type
        }
        if self.user_type == "bidder":
            data["bidders"] = []

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            email=data.get("email"),
            password=data.get("password"),
            _id=data.get("_id")
        )
