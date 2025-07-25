from flask import Flask
app = Flask(__name__)

# VULNERABLE: Weak secret key
app.config['SECRET_KEY'] = 'hardcoded-secret-123'
app.config['SESSION_COOKIE_HTTPONLY'] = False  # UNSAFE: Allows JS cookie access