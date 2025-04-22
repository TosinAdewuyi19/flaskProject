from enum import Enum

class UserType(Enum):
    SELLER = "seller"
    BIDDER = "bidder"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
