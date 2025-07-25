from app import app

# VULNERABLE: Runs with debug mode enabled
app.run(host='0.0.0.0', port=5000, debug=True)