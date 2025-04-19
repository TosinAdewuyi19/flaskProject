from Demos.win32ts_logoff_disconnected import username
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_user(self):
        db.users.insert_one({
            'username': self.username,
            'email': self.email,
            'password': self.password
        })

    @staticmethod
    def authenticate_user(email, password):
        user = db.users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            return user
        return None