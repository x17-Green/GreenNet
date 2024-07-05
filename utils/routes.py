# routes.py
from flask import Blueprint, redirect, url_for, request, render_template, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from flask_bcrypt import Bcrypt

from.backup_utils import create_backup, restore_backup
from.ftp_utils import FTPConnection
from config.config import Config  # Import the Config object
from.db import db
from models.user import User
# from app import bcrypt

from.reg_form import RegistrationForm
from.login_form import LoginForm

# from flask_principal import Principal, RoleNeed, UserNeed # roles_required

routes_bp = Blueprint('routes', __name__)

# Initialize Flask-Login
login_manager = LoginManager()

# # Initialize Flask-Principal
# principals = Principal(routes_bp)

# # Define roles
# admin_role = RoleNeed('admin')


@login_manager.user_loader
def load_user(user_id):
    # Implement user loading logic here
    return User.query.get(int(user_id))

@routes_bp.route("/")
def index():
    return render_template('index.html')

@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('routes.dashboard'))
    return render_template('login/index.html', form=form)

@routes_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard/index.html')

@routes_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@routes_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('routes.login'))
    return render_template('register/index.html', form=form)


@routes_bp.route('/backup', methods=['GET', 'POST'])
def create_backup_route():
    backup_file = 'backup.sql'
    create_backup(backup_file)  # Call the create_backup function from backup_utils
    return jsonify({'message': 'Backup created successfully'})

@routes_bp.route('/restore', methods=['GET', 'POST'])
def restore_backup_route():
    backup_file = 'backup.sql'
    restore_backup(backup_file)  # Call the restore_backup function from backup_utils
    return jsonify({'message': 'Backup restored successfully'})

# FTP Upload Link
@routes_bp.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    ftp_connection = FTPConnection()
    ftp_connection.upload_file()
    ftp_connection.close_connection()
    return 'File uploaded successfully!'

