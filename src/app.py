from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from config import Config
from src.controllers.auth_controller import auth_bp
from src.controllers.bidders_controller import bidders_bp
from src.controllers.sellers_controller import sellers_bp
from src.controllers.listings_controller import product_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)

app.register_blueprint(bidders_bp, url_prefix="/bidders")

app.register_blueprint(sellers_bp, url_prefix="/sellers")

app.register_blueprint(product_bp, url_prefix="/products")


if __name__ == '__main__':
    app.run(debug=True)
