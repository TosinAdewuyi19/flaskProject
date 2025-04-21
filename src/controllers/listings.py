from flask import Blueprint, request, jsonify
from src.services.product_service import ProductService
from src.dto.product_dto import ProductDTO
from src.exceptions.custom_exceptions import BadRequestError

product_bp = Blueprint('products', __name__)
product_service = ProductService()

@product_bp.route('/create', methods=['POST'])
def create_product():
    try:
        data = request.json
        product_dto = ProductDTO.from_dict(data)
        result = product_service.create_product(product_dto)
        return jsonify({"message": "Product listed", "data": result}), 201
    except BadRequestError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

@product_bp.route('/', methods=['GET'])
def list_all_products():
    products = product_service.get_all_products()
    return jsonify(products), 200
