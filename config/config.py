import os
from dotenv import load_dotenv

load_dotenv() # Load the .env file to set environment variables.

class Config:
    """App config settings"""
    # Database Connection
    DB_USERNAME = os.getenv('HDB_USERNAME')
    DB_PASSWORD = os.getenv('HDB_PASSWORD')
    DB_HOST = os.getenv('HDB_HOST')
    DB_PORT = os.getenv('HDB_PORT')
    DB_NAME = os.getenv('HDB_NAME')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Console credentials
    ADMIN_USERNAME = os.getenv('CONSOLE_USERNAME')
    ADMIN_PASSWORD = os.getenv('CONSOLE_PASSWORD')
    DEBUG = os.getenv('DEBUG', False)

    # Backup Dir
    BACKUP_DIR = os.getenv('BACKUP_DIR')

    # Google Auth Credentials
    GOOGLE_CLIENT_ID = os.getenv('client_id')
    GOOGLE_CLIENT_SECRET = os.getenv('client_secret')

    # FTP Link
    FTP_SERVER = os.getenv('FTP_SERVER')
    FTP_USERNAME = os.getenv('FTP_USERNAME')
    FTP_PASSWORD = os.getenv('FTP_PASSWORD')
    FTP_PORT = os.getenv('FTP_PORT')
    REMOTE_FILE_PATH = os.getenv('FTP_DIR')