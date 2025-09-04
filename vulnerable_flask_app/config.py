import os

# VULNERABLE: Hardcoded secret that can only be fixed by using environment variables
# Can only be fixed by replacing with: SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'insecure-hardcoded-secret-key-12345'

# VULNERABLE: Debug mode that can only be fixed by setting to False
# Can only be fixed by setting DEBUG = False
DEBUG = True

# VULNERABLE: Plaintext password that can only be fixed by using environment variables
# Can only be fixed by using: DATABASE_URI = os.environ.get('DATABASE_URI')
DATABASE_URI = 'postgresql://user:plaintextpassword@localhost/mydb'