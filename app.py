from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from .auth import auth_bp
from .listings import listings_bp
from .bids import bids_bp



app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db= client["auction_db"]

app.config["JWT_SECRET_KEY"] = "YOUR_SECRET_KEY"
JWT = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(listings_bp)
app.register_blueprint(bids_bp)

if __name__ == '__main__':
    app.run()
