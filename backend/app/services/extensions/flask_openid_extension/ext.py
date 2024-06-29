from flask import current_app, redirect, url_for
from flask_openid import OpenID

class FlaskOpenIDExtension:
    
    def __init__(self, app=None):
        self.openid = OpenID(app)
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Initialize the OpenID extension with the app
        app.config.setdefault('OPENID_FS_STORE_PATH', '/tmp')
        self.openid = OpenID(app, self.store_path())

    def store_path(self):
        # Return the path to store OpenID data
        return current_app.config['OPENID_FS_STORE_PATH']

    def login(self, return_to):
        # A sample method that can be called from the Flask app to initiate OpenID login
        self.openid.try_login('https://example.com', ask_for=['email', 'fullname'])
        return redirect(url_for(return_to))

    def get_user_info(self, openid_response):
        # A sample method that can be called from the Flask app to get user info from OpenID response
        return openid_response.fullname, openid_response.email
