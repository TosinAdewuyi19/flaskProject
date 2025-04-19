from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db= client["auction_db"]

app.config["JWT_SECRET_KEY"] = "YOUR_SECRET_KEY"
JWT = JWTManager(app)

from controllers.user_controller import user_bp
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()
