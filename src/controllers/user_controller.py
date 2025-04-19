from flask import Blueprint, request,jsonify
from services.userServices import UserServices

user_controller = Blueprint('user_controller', __name__)
user_services = UserServices()

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = user_services.register_user(data["username"], data["password"], data["email"])
    return jsonify({"message": "User registered successfully!", "username": user.username})

@user_controller.route('/login', methods=['POST'])
def login():
    data = request.json
    user = user_services.login_user(data["username"], data["password"], data["email"])
    if user:
        return jsonify({"message": "User logged in!", "username": user["username"]})
    else:
        return jsonify({"message": "Invalide username or password!"}) 