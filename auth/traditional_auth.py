import hashlib
import json

def load_users(file_path='users.json'):
    users = {}
    try:
        with open(file_path, 'r') as f:
            raw = json.load(f)
            for username, plain_password in raw.items():
                hashed = hashlib.sha256(plain_password.encode()).hexdigest()
                users[username] = hashed
    except Exception as e:
        print("Error loading users:", e)
    return users

users = load_users()

def authenticate(credential_input):
    """Expects 'username:password'"""
    try:
        username, password = credential_input.split(":", 1)
        stored_hash = users.get(username.strip())
        if not stored_hash:
            return False
        return hashlib.sha256(password.strip().encode()).hexdigest() == stored_hash
    except Exception:
        return False

