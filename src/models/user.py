from werkzeug.security import generate_password_hash, check_password_hash
from app import db


def create_user(self):
        db.users.insert_one({
            'username': self.username,
            'email': self.email,
            'password': self.password
        })


def find_user_by_email(email, password):
       return db.users.find_one({'email': email, 'password': password})

def check_user_password(self, user, password):
        return check_password_hash(user['password'], password)