#!/usr/bin/python3

from flask import Flask, jsonify
from flask_migrate import Migrate

from config.config import Config  # Imports my configuration script
from utils.routes import routes_bp, login_manager  # Import the routes blueprint, login manager
from utils.db import db  # Imports my database link
from models import user, device, device_data, notification, notification_history, notification_setting, notification_threshold  # Imports all my model classes

# Initializes the flask framework
app = Flask(
    __name__, 
    template_folder='templates', 
    static_url_path='/static', 
    static_folder='static'
    )

app.config.from_object(Config)  # Links the app to the config file
db.init_app(app)  # Initialise the database connection
migrate = Migrate(app, db)  # Set up database migrations
app.register_blueprint(routes_bp) # Register the routes blueprint

# Initialize Flask-Login
login_manager.init_app(app)
login_manager.login_view = 'login'

# Create all tables within the application context
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3440, debug=True)