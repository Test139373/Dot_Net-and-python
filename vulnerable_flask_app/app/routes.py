from flask import Flask, request, render_template_string, send_file
import yaml
import requests
from jinja2 import Template, Environment
from PIL import Image, EpsImagePlugin
import io
import sqlalchemy
from sqlalchemy import text

app = Flask(__name__)

# VULNERABLE: CVE-2020-1747 - PyYAML unsafe deserialization
# Can only be fixed by replacing yaml.load() with yaml.safe_load()
@app.route('/yaml', methods=['POST'])
def yaml_deserialize():
    data = request.get_data()
    # VULNERABLE: Must be replaced with yaml.safe_load()
    result = yaml.load(data, Loader=yaml.Loader)
    return str(result)

# VULNERABLE: CVE-2021-38314 - PyYAML custom unsafe loader
# Can only be fixed by not using UnsafeLoader
@app.route('/yaml-unsafe-loader', methods=['POST'])
def yaml_unsafe_loader():
    data = request.get_data()
    # VULNERABLE: Must remove UnsafeLoader usage
    result = yaml.load(data, Loader=yaml.UnsafeLoader)
    return str(result)

# VULNERABLE: CVE-2024-22195 - Jinja2 SSTI
# Can only be fixed by using Template.escape() or sanitization
@app.route('/render-unsafe')
def render_template_unsafe():
    user_input = request.args.get('input', '')
    # VULNERABLE: Must be replaced with Template.escape() or sanitized input
    template = Template(f"Hello {user_input}!")
    return template.render()

# VULNERABLE: CVE-2020-28493 - Jinja2 sandbox bypass
# Can only be fixed by using SandboxedEnvironment
@app.route('/render-sandbox-bypass')
def render_sandbox_bypass():
    user_input = request.args.get('input', '')
    # VULNERABLE: Must be replaced with SandboxedEnvironment
    env = Environment()
    template = env.from_string(user_input)
    return template.render()

# VULNERABLE: CVE-2023-32681 - Requests SSRF with verify=False
# Can only be fixed by setting verify=True or using proper certificate validation
@app.route('/fetch-insecure')
def fetch_url_insecure():
    url = request.args.get('url', '')
    # VULNERABLE: Must set verify=True and implement proper URL validation
    response = requests.get(url, verify=False)
    return response.text

# VULNERABLE: CVE-2018-18074 - Requests with unlimited redirects
# Can only be fixed by setting allow_redirects=False or limiting redirects
@app.route('/redirect-unlimited')
def follow_unlimited_redirects():
    url = request.args.get('url', '')
    # VULNERABLE: Must set allow_redirects=False or implement redirect limits
    response = requests.get(url, allow_redirects=True)
    return response.text

# VULNERABLE: CVE-2022-45198 - Pillow with vulnerable image processing
# Can only be fixed by using Image.ANTIALIAS instead of Image.NEAREST for resizing
@app.route('/process-image-unsafe', methods=['POST'])
def process_image_unsafe():
    if 'image' not in request.files:
        return 'No image uploaded'
    
    image_file = request.files['image']
    img = Image.open(image_file.stream)
    
    # VULNERABLE: Must replace Image.NEAREST with Image.ANTIALIAS for safe resizing
    img = img.resize((100, 100), Image.NEAREST)
    
    output = io.BytesIO()
    img.save(output, format='JPEG')
    return send_file(output, mimetype='image/jpeg')

# VULNERABLE: CVE-2021-25287 - Pillow EPS processing with vulnerable plugin
# Can only be fixed by disabling EPS support or using safe EPS handling
@app.route('/process-eps-unsafe', methods=['POST'])
def process_eps_unsafe():
    if 'eps' not in request.files:
        return 'No EPS file uploaded'
    
    eps_file = request.files['eps']
    # VULNERABLE: Must disable EPS support or use safe EPS handling methods
    EpsImagePlugin.ghostscript = None  # Disabling safety check
    img = Image.open(eps_file.stream)
    
    output = io.BytesIO()
    img.save(output, format='PNG')
    return send_file(output, mimetype='image/png')

# VULNERABLE: CVE-2022-29361 - Flask with debug mode enabled
# Can only be fixed by setting debug=False
@app.route('/debug-info')
def debug_info():
    # VULNERABLE: Must set app.debug = False in main application
    if app.debug:
        return "Debug mode is enabled - this is vulnerable!"
    return "Debug mode is disabled"

# VULNERABLE: CVE-2018-1000656 - Flask session not regenerated
# Can only be fixed by using session.regenerate() or proper session management
@app.route('/login-unsafe')
def login_unsafe():
    username = request.args.get('username')
    # VULNERABLE: Must implement session regeneration on login
    session['username'] = username
    return f"Logged in as {username} (session not regenerated)"