from src.data.models.usertype import UserType


class User:
    def __init__(self, name, email, password, user_type, _id=None):
        if user_type not in UserType.list():
            raise TypeError(f"Invalid user type: {user_type}")

        self._id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type

    def to_dict(self):
        data = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "user_type": self.user_type
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            email=data.get("email"),
            password=data.get("password"),
            user_type=data.get("user_type"),
            _id=data.get("_id")
        )
