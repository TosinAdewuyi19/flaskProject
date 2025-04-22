from flask import Blueprint, request, jsonify
from src.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_service = AuthService()

@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        user = auth_service.register(request.json)
        return jsonify({"message": "User registered successfully", "user": user}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        user = auth_service.login(email, password)
        return jsonify({"message": "Login successful", "user": user}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 401
