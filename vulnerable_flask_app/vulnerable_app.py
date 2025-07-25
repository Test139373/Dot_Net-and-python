#!/usr/bin/env python3
import os
import pickle
import subprocess
from flask import Flask, request, render_template_string
import yaml  # PyYAML
import jinja2  # Jinja2
import django  # Django (for SQL injection example)
from cryptography.fernet import Fernet  # cryptography (weak crypto example)

app = Flask(__name__)

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
    name = request.args.get('name', 'Guest')
    # UNSAFE: Server-Side Template Injection
    template = f"Hello {name}! 7*7 = {{7*7}}"
    return render_template_string(template)

# VULNERABLE: CVE-2022-34265 - Pickle RCE
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

# VULNERABLE: CWE-327 - Weak Cryptography
@app.route('/encrypt')
def weak_encrypt():
    # UNSAFE: Using hardcoded key
    key = Fernet.generate_key()
    cipher = Fernet(key)
    text = request.args.get('text', 'secret')
    return cipher.encrypt(text.encode())

# VULNERABLE: CWE-89 - SQL Injection
@app.route('/search')
def sql_injection():
    query = request.args.get('query', '1')
    # UNSAFE: Concatenated SQL query
    cmd = f"sqlite3 database.db 'SELECT * FROM users WHERE id = {query}'"
    return subprocess.getoutput(cmd)

if __name__ == '__main__':
    app.run(debug=True)  # UNSAFE: Debug mode in production