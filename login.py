import hashlib

users = {
    "admin": {"password": hashlib.sha256("admin123".encode()).hexdigest(), "role": "admin"},
    "user": {"password": hashlib.sha256("user123".encode()).hexdigest(), "role": "user"}
}

def verify_login(username, password, otp_code=None):
    if username in users:
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        if hashed_pw == users[username]["password"]:
            return True, users[username]["role"]
        return False, "Invalid password"
    return False, "Invalid username"
