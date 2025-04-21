from flask import Blueprint, request, jsonify
from src.services.seller_service import SellerService
from src.dto.seller_dto import SellerDTO
from src.exceptions.custom_exceptions import BadRequestError

sellers_bp = Blueprint('sellers', __name__)
seller_service = SellerService()

@sellers_bp.route('/register', methods=['POST'])
def register_seller():
    try:
        data = request.json
        seller_dto = SellerDTO.from_dict(data)
        result = seller_service.register_seller(seller_dto)
        return jsonify({"message": "Seller registered", "data": result}), 201
    except BadRequestError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

@sellers_bp.route('/<seller_id>', methods=['GET'])
def get_seller(seller_id):
    seller = seller_service.get_seller_by_id(seller_id)
    if seller:
        return jsonify(seller), 200
    return jsonify({"error": "Seller not found"}), 404
