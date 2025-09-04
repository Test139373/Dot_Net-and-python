#!/usr/bin/env python3
"""
Vulnerable Python Application for Security Testing
Main application entry point with intentionally vulnerable configurations
"""

from app import app
import os

# Additional vulnerable configurations
app.config.update(
    # VULNERABLE: Debug mode enabled in production
    DEBUG=True,
    
    # VULNERABLE: Hardcoded secret key
    SECRET_KEY='insecure-hardcoded-secret-key-12345',
    
    # VULNERABLE: Disabled security features
    SESSION_COOKIE_HTTPONLY=False,
    SESSION_COOKIE_SECURE=False,
    
    # VULNERABLE: Large file upload allowed
    MAX_CONTENT_LENGTH=100 * 1024 * 1024,  # 100MB
)

# Import all vulnerable route modules to ensure they're registered
from app import routes
from app import deserialization_vulns
from app import file_handling_vulns
from app import network_vulns
from app import parsing_vulns
from app import crypto_vulns
from app import command_exec_vulns
from app import data_processing_vulns

# VULNERABLE: Additional insecure configuration
# Disable strict transport security
app.config['PREFERRED_URL_SCHEME'] = 'http'

if __name__ == '__main__':
    # VULNERABLE: Running on all interfaces with debug mode
    # This exposes the application to the network
    app.run(
        host='0.0.0.0',  # Binds to all network interfaces
        port=5000,
        debug=True,      # Debug mode enabled (security risk)
        threaded=True    # No thread limit (potential resource exhaustion)
    )