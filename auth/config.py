import os
# config.py
AUTH_METHOD = 'traditional_auth'  # or 'zkp_auth'

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
USER_DB_PATH = os.path.join(BASE_DIR, "users.json")

# Flask secret key
SECRET_KEY = "supersecurekey"  
