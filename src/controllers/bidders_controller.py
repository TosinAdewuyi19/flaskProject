from flask import Blueprint, request, jsonify
from src.services.bidder_service import BidderService
from src.dto.bidder_dto import BidderDTO
from src.exceptions.custom_exceptions import BadRequestError

bidders_bp = Blueprint('bidders', __name__)
bidder_service = BidderService()

@bidders_bp.route('/register', methods=['POST'])
def register_bidder():
    try:
        data = request.json
        bidder_dto = BidderDTO.from_dict(data)
        result = bidder_service.register_bidder(bidder_dto)
        return jsonify({"message": "Bidder registered", "data": result}), 201
    except BadRequestError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

@bidders_bp.route('/<bidder_id>', methods=['GET'])
def get_bidder(bidder_id):
    bidder = bidder_service.get_bidder_by_id(bidder_id)
    if bidder:
        return jsonify(bidder), 200
    return jsonify({"error": "Bidder not found"}), 404
