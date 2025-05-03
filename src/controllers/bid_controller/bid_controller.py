from flask import Blueprint, request, jsonify

from src.services.bid_service.bid_service import bid_service

bid_controller = Blueprint('bid_controller', __name__)

@bid_controller.route('/bids', methods=['POST'])
def place_bid():
    bid_data = request.json
    try:
        bid = bid_service.create_bid(bid_data)
        return jsonify(bid=bid, message="Bid created successfully!"), 201
    except ValueError as e:
        return jsonify(error=str(e)), 400

@bid_controller.route('/bids/auction/<auction_id>', methods=['GET'])
def get_bids_by_auction(auction_id):
    bids = bid_service.get_bids_by_auction(auction_id)
    return jsonify(bids=bids)

@bid_controller.route('/bids/<int:bid_id>', methods=['DELETE'])
def delete_bid(bid_id):
    try:
        bid = bid_service.delete_bid(bid_id)
        return jsonify(message="Bid deleted successfully!", bid=bid), 200
    except ValueError as e:
        return jsonify(error=str(e)), 404