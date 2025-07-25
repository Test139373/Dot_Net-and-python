from flask import Flask, request, render_template, make_response
import pickle
import yaml
import subprocess
from app import app  # Import Flask app instance
import os

# VULNERABLE: CVE-2020-1747 - PyYAML unsafe load
@app.route('/yaml', methods=['POST'])
def yaml_load():
    data = request.get_data()
    # UNSAFE: Allows arbitrary code execution
    loaded = yaml.load(data, Loader=yaml.Loader)  # Dangerous loader
    return str(loaded)

# VULNERABLE: CVE-2024-22195 - Jinja2 SSTI
@app.route('/ssti')
def ssti():
    user_input = request.args.get('input', '<script>alert(1)</script>')
    # UNSAFE: Server-Side Template Injection
    return render_template('index.html', user_input=user_input)

# VULNERABLE: CWE-502 - Pickle RCE
@app.route('/pickle', methods=['POST'])
def pickle_load():
    data = request.get_data()
    # UNSAFE: Arbitrary code execution via pickle
    return str(pickle.loads(data))

# VULNERABLE: CWE-78 - OS Command Injection
@app.route('/cmd')
def run_cmd():
    cmd = request.args.get('cmd', 'whoami')
    # UNSAFE: Shell command injection
    return subprocess.getoutput(cmd)

# VULNERABLE: CWE-312 - Cleartext Storage
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')  # UNSAFE: Plaintext password
    return f"Logged in as {username} with password {password}"

# VULNERABLE: CWE-798 - Hardcoded Credentials
@app.route('/admin')
def admin():
    # UNSAFE: Hardcoded credentials
    if request.args.get('token') == "admin123":
        return "Admin panel accessed"
    return "Access denied"

# VULNERABLE: CWE-352 - CSRF (Missing Token)
@app.route('/transfer', methods=['POST'])
def transfer_money():
    amount = request.form.get('amount')
    return f"Transferred ${amount} without CSRF checks"

# VULNERABLE: CWE-117 - Improper Error Handling
@app.route('/debug')
def debug():
    try:
        1/0  # Force error
    except Exception as e:
        return str(e)  # UNSAFE: Exposes stack trace