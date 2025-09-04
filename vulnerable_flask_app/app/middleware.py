from flask import request, Response

# VULNERABLE: CORS middleware that allows any origin
# Can only be fixed by specifying specific origins
@app.after_request
def add_cors_headers(response):
    # VULNERABLE: Must replace '*' with specific allowed origins
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# VULNERABLE: Authentication with hardcoded token
# Can only be fixed by implementing proper token validation
@app.before_request
def check_auth():
    if request.endpoint in ['login', 'static']:
        return
    
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return Response('Unauthorized', status=401)
    
    # VULNERABLE: Must implement proper token validation instead of hardcoded check
    token = auth_header[7:]
    if token != 'hardcoded-secret-token':
        return Response('Invalid token', status=401)