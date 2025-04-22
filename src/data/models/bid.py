from datetime import datetime

class Bid:
    def __init__(self, bidder_id, product_id, amount, timestamp=None, _id=None):
        self._id = str(_id) if _id else None
        self.bidder_id = bidder_id
        self.product_id = product_id
        self.amount = float(amount)
        self.timestamp = timestamp or datetime.utcnow()

    def to_dict(self):
        data = {
            "bidder_id": self.bidder_id,
            "product_id": self.product_id,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            bidder_id=data.get("bidder_id"),
            product_id=data.get("product_id"),
            amount=data.get("amount"),
            timestamp=data.get("timestamp"),
            _id=data.get("_id")
        )
