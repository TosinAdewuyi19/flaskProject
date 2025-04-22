import re

class Validator:
    @staticmethod
    def is_email_valid(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def is_password_strong(password):
        return len(password) >= 6  # you can make this stricter

    @staticmethod
    def validate_required_fields(data, fields):
        missing = [field for field in fields if field not in data]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
