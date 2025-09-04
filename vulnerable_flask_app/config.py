import os

# Insecure configurations
DEBUG = True
SECRET_KEY = 'insecure-secret-key'
DATABASE_URI = 'sqlite:///test.db'

# Disabled security features
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False