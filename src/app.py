from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from config import Config

socketio = SocketIO(cors_allowed_origins="*")
mongo = PyMongo()

def create_app():
    app = Flask(__name__, template_folder="../external_templates")
    app.config.from_object(Config)

    mongo.init_app(app)
    socketio.init_app(app)

    # Import and register blueprints
    from src.controllers.bidders_controller import bidders_bp
    from src.controllers.sellers_controller import sellers_bp
    from src.controllers.product_controller import product_bp

    app.register_blueprint(bidders_bp, url_prefix="/bidders")
    app.register_blueprint(sellers_bp, url_prefix="/sellers")
    app.register_blueprint(product_bp, url_prefix="/products")

    return app
