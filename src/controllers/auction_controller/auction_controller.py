from flask import Blueprint
from flask import request
from flask import jsonify

from src.services.auction_service.auction_service import auction_service

auction_controller = Blueprint('auction_controller', __name__)

@auction_controller.route('/auctions', methods=['POST'])
def create_auction():
    auction_data = request.json
    auction_service.create_auction(auction_data)
    return jsonify(message="Auction created successfully!"), 201

@auction_controller.route('/auctions/seller/<seller>', methods=['GET'])
def get_auctions_by_seller(seller):
    auctions = auction_service.get_auctions_by_seller(seller)
    return jsonify(auctions=auctions)

@auction_controller.route('/auctions', methods=['GET'])
def get_all_auctions():
    auctions = auction_service.get_all_auctions()
    return jsonify(auctions=auctions)

@auction_controller.route('/auctions/<int:auction_id>', methods=['DELETE'])
def delete_auction(auction_id):
    try:
        auction = auction_service.delete_auction(auction_id)
        return jsonify(message="Auction deleted successfully!", auction=auction), 200
    except ValueError as e:
        return jsonify(error=str(e)), 404
