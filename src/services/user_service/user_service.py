from src.data.repositories.user_repo.user_repo import UserRepository

class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, user_data):
        if not user_data or 'username' not in user_data or 'email' not in user_data:
            raise ValueError("User data must include 'username' and 'email'.")

        if any(user['username'] == user_data['username'] for user in self.users):
            raise ValueError("Username already exists.")
        if any(user['email'] == user_data['email'] for user in self.users):
            raise ValueError("Email already exists.")


        user_id = len(self.users) + 1
        user = {
        "id": user_id,
        "username": user_data['username'],
        "email": user_data['email'],
        "full_name": user_data.get('full_name', "")
    }
        self.users.append(user)
        print("User created:", user)
        return user


def get_user(self, user_id):
    for user in self.users:
        if user['id'] == user_id:
            return user
    raise ValueError("User not found.")

def delete_user(self, user_id):
    for user in self.users:
        if user['id'] == user_id:
            self.users.remove(user)
            print("User deleted:", user)
            return user
    raise ValueError("User not found.")

user_service = UserService()
