# src/app.py

from flask import Flask
from src.controllers.auction_controller.auction_controller import auction_controller
from src.controllers.bid_controller.bid_controller import bid_controller
from src.controllers.user_controller.user_controller import user_controller

def create_app():
    app = Flask(__name__)


    app.register_blueprint(auction_controller, url_prefix='/api')
    app.register_blueprint(bid_controller, url_prefix='/api')
    app.register_blueprint(user_controller, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Enable debug mode for better error reporting
