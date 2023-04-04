import os
import secrets

class Config:
    # Use a cryptographically secure random key for the SECRET_KEY
    SECRET_KEY = secrets.token_urlsafe(16)

    # Use a secret management tool like HashiCorp Vault or AWS Secrets Manager to store database credentials
    DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
    DATABASE_HOST = os.environ.get('DATABASE_HOST')
    DATABASE_PORT = os.environ.get('DATABASE_PORT')
    DATABASE_NAME = os.environ.get('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    # Use a dedicated logging system instead of echoing SQL statements to the console
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')
    LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    LOGGING_LOCATION = 'app.log'

    # Add security features like password hashing, session management, and CSRF protection
    # See Flask-Login, Flask-Session, and Flask-WTF extensions for more details
    # ...

    # Disable tracking modifications to models for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False
