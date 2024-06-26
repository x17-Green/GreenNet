#!/usr/bin/python3
# App Config script

from config.config import Config  # Imports my configuration script
from utils.db import db  # Imports my database link
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Initializes the flask framework
app.config.from_object(Config)  # Links the app to the config file

db.init_app(app)  # Initialise the database connection
migrate = Migrate(app, db)  # Set up database migrations

from models import *  # Imports all my model classes

# Create all tables within the application context
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return f'Welcome to GreenNet'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3440, debug=True)