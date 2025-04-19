from flask import Blueprint, jsonify, request
from services.auction_services import AuctionServices

auction_bp = Blueprint('auction', __name__)
auction_services = AuctionServices()

@auction_bp.route('/list', methods=['GET'])
def list_actions():
    auctions = auction_services.get_auctions()
    return jsonify(auctions)

@auction_bp.route('/create', methods=['POST'])
def create_action():
    data = request.json()
    auction = auction_services.create_auction(data["item_name"], data["starting_bid"], data["end_time"])
    return jsonify({"message":"Auction created successfully"})