import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"

class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "database.sqlite3")
    DEBUG = False
    SECRET_KEY =  'some-secret-key'
    SECURITY_PASSWORD_HASH = "bcrypt"    
    SECURITY_PASSWORD_SALT = "really super secret" # Read from ENV in your case
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_POST_LOGIN_VIEW = '/dashboard/email'
    WTF_CSRF_ENABLED = False
    # SECURITY_URL_PREFIX = '/api/accounts'
    # # SECURITY_POST_CONFIRM_VIEW = "/confirmed"
    # # SECURITY_CONFIRM_ERROR_VIEW = "/confirm-error"
    # # SECURITY_RESET_VIEW = "/reset-password"
    # # SECURITY_RESET_ERROR_VIEW = "/reset-password"
    # SECURITY_REDIRECT_BEHAVIOR = "spa"
    # SECURITY_CSRF_PROTECT_MECHANISMS = ["session", "basic"]
    # SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True
    SECURITY_REDIRECT_HOST = 'localhost:8080'
