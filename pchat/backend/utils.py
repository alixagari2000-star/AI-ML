def is_valid_username(username: str) -> bool:
    return username.isalnum() and len(username) >= 3
