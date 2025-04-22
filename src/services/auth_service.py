from werkzeug.security import generate_password_hash, check_password_hash
from src.data.user import User
from src.dto.user_dto import UserDTO
from src.repositories.user_repo import UserRepo

class AuthService:
    def __init__(self):
        self.user_repo = UserRepo()

    def register(self, data):
        dto = UserDTO(data)

        # Check if email already exists
        if self.user_repo.find_by_email(dto.email):
            raise ValueError("Email already registered")

        # Hash password
        hashed_password = generate_password_hash(dto.password)

        # Create user object
        user = User(
            name=dto.name,
            email=dto.email,
            password=hashed_password,
            user_type=dto.user_type
        )

        return self.user_repo.create(user)

    def login(self, email, password):
        user_data = self.user_repo.find_by_email(email)
        if not user_data:
            raise ValueError("Invalid email or password")

        if not check_password_hash(user_data["password"], password):
            raise ValueError("Invalid email or password")

        return user_data
