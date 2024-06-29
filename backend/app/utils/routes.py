#!/usr/bin/python3
# Routes configuration file

from flask import Blueprint, redirect, url_for, request, render_template
from services.extensions.flask_openid_extension.ext import FlaskOpenIDExtension

routes_bp = Blueprint('routes', __name__)

@routes_bp.route("/")
def index():
    return render_template('landing.html')

# Initialize the FlaskOpenIDExtension
openid_ext = FlaskOpenIDExtension()

@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return_to = url_for('routes.after_login', _external=True)
        return openid_ext.login(return_to)
    return '''
        <form action="" method="post">
            <input type="submit" value="Login with OpenID">
        </form>
    '''

@routes_bp.route('/after_login')
def after_login():
    openid_response = openid_ext.openid.get_response()
    if openid_response.status == 'success':
        fullname, email = openid_ext.get_user_info(openid_response)
        return f'Welcome, {fullname} ({email})!'
    return 'Invalid OpenID response'
