from flask_pymongo import PyMongo

class UserRepository:
    def __init__(self, mongo: PyMongo):
        self.mongo = mongo

    def find_user_by_username(self, username):
        return self.mongo.db.users.find_one({'username': username})

    def create_user(self, user_data):
        self.mongo.db.users.insert_one(user_data)
