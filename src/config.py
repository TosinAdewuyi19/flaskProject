import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/auction_db')
