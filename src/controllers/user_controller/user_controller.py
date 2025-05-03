from flask import Blueprint, request, jsonify

from src.services.user_service.user_service import user_service, UserService

user_service = UserService()
user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=['POST'])
def register():
    user_data = request.json
    try:
        user = user_service.create_user(user_data)
        return jsonify(user=user, message="User created successfully!"), 201
    except ValueError as e:
        return jsonify(error=str(e)), 400

@user_controller.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = user_service.authenticate_user(username, password)
    if user:

        return jsonify(message="Login successful!")
    return jsonify(message="Invalid credentials"), 401


@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = user_service.delete_user(user_id)
        return jsonify(message="User deleted successfully!", user=user), 200
    except ValueError as e:
        return jsonify(error=str(e)), 404

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_service.get_user(user_id)
        return jsonify(user=user)  # Return the user information
    except ValueError as e:
        return jsonify(error=str(e)), 404
