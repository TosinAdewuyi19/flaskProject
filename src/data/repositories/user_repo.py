from src.db import get_db
from src.data.user import User

class UserRepo:
    def __init__(self):
        self.collection = get_db().users  # MongoDB collection

    def create(self, user: User):
        user_dict = user.to_dict()
        result = self.collection.insert_one(user_dict)
        user_dict["_id"] = str(result.inserted_id)
        return user_dict

    def find_by_email(self, email):
        user = self.collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])
        return user
