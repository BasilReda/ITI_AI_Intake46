import re
from dataclasses import dataclass

@dataclass
class UserRegistrationData:
    username: str
    email: str
    password: str

def validate_registration(data: UserRegistrationData) -> list[str]:
    """
    Validates user registration data.
    Returns a list of validation error messages. If the list is empty, the data is valid.
    """
    errors = []
    
    if not _is_valid_username(data.username):
        errors.append("Username must be 3-20 alphanumeric characters.")
        
    if not _is_valid_email(data.email):
        errors.append("Invalid email format.")
        
    if not _is_valid_password(data.password):
        errors.append("Password must be at least 8 characters, with 1 uppercase, 1 lowercase, and 1 number.")
        
    return errors

def _is_valid_username(username: str) -> bool:
    """Validates that the username is 3-20 characters long and contains only alphanumeric characters."""
    return bool(re.match(r"^[a-zA-Z0-9]{3,20}$", username))

def _is_valid_email(email: str) -> bool:
    """Validates that the email has a valid format."""
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

def _is_valid_password(password: str) -> bool:
    """Validates that the password meets the required criteria."""
    has_length = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    
    return all([has_length, has_upper, has_lower, has_digit])
