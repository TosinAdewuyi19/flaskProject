class Product:
    def __init__(self, title, description, starting_price, seller_id, _id=None):
        self._id = str(_id) if _id else None
        self.title = title
        self.description = description
        self.starting_price = float(starting_price)
        self.seller_id = seller_id

    def to_dict(self):
        data = {
            "title": self.title,
            "description": self.description,
            "starting_price": self.starting_price,
            "seller_id": self.seller_id
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            description=data.get("description"),
            starting_price=data.get("starting_price"),
            seller_id=data.get("seller_id"),
            _id=data.get("_id")
        )
