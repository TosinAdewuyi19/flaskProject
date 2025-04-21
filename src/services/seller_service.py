from src.data.models.seller import User

class UserService:
    def register_user(self, username, email, password):
        user = User(username, email, password)
        user.save_to_db()
        return user

    def login_user(self, username, email, password):
        return User.authenticate(email, password)