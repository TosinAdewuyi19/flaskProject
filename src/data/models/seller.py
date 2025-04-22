class Seller:
    def __init__(self, name, email, store_name, password, _id=None):
        self._id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.store_name = store_name
        self.password = password

    def to_dict(self):
        data = {
            "name": self.name,
            "email": self.email,
            "store_name": self.store_name,
            "password": self.password
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            email=data.get("email"),
            store_name=data.get("store_name"),
            password=data.get("password"),
            _id=data.get("_id")
        )
