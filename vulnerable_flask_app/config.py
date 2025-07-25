# INSECURE CONFIGURATIONS
import os

class Config:
    # VULNERABLE: Hardcoded secrets
    SECRET_K = 'dont-use-this-in-production-123'  # CWE-798
    ADMIN_PASSWORD = 'admin@123'  # CWE-259
    
    # VULNERABLE: Debug mode enabled
    DEBUG = True  # CWE-489
    
    # VULNERABLE: Database config with plaintext password
    DATABASE_URI = 'postgresql://user:password@localhost/db'  # CWE-521
    
    # VULNERABLE: Disabled security headers
    DISABLE_CSRF = True  # CWE-352
    DISABLE_CORS = True  # CWE-942
    
    # VULNERABLE: File upload settings
    UPLOAD_FOLDER = '/tmp/uploads'
    ALLOWED_EXTENSIONS = {'exe', 'sh', 'php'}  # CWE-434


}