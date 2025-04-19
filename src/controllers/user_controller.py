from flask import Blueprint, request,jsonify
from services.user_service import user

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = user_service.register_user(data["username"], data["password"], data["email"])
    return jsonify({"message": "User registered successfully!", "username": user.username})

@user_controller.route('/login', methods=['POST'])
def login():
    data = request.json
    user = user_service.login_user(data["username"], data["password"], data["email"])
    if user:
        return jsonify({"message": "User logged in!", "username": user["username"]})
    else:
        return jsonify({"message": "Invalid username or password!"})