"""
Vulnerable Security App Package

This package contains intentionally vulnerable code for security testing purposes.
All vulnerabilities are documented with their respective CVE IDs and descriptions.
"""

from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Import all vulnerable modules to make them available
from . import deserialization_vulns
from . import file_handling_vulns
from . import network_vulns
from . import parsing_vulns
from . import crypto_vulns
from . import command_exec_vulns
from . import data_processing_vulns
from . import routes

# Load configuration
app.config.from_pyfile('../config.py')

# Import routes after app creation to avoid circular imports
from .routes import *