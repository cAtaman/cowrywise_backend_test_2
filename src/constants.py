import os

CLIENT_HOST = os.getenv("CLIENT_HOST", "0.0.0.0")
CLIENT_PORT = os.getenv("CLIENT_PORT", 1759)

ADMIN_HOST = os.getenv("ADMIN_HOST", "0.0.0.0")
ADMIN_PORT = os.getenv("ADMIN_PORT", 1800)
