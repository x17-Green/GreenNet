#!/usr/bin/python3
# Console for the GreenNet User Authentication System

import os
import platform
import cmd2
import colorama
import datetime
import getpass

from app import app
from utils.db import db
from config.config import Config
from models.user import User
# notification, notification_threshold, notification_setting, notification_history, device, device_data

app.app_context().push()

class GreenNetCMD(cmd2.Cmd):
    """GreenNet User Authentication System console.

    This class provides a command-line interface for 
    interacting with the GreenNet system.
    """
    intro = "\nWelcome to the GreenNet User Authentication System\nv.1.0\n\nType help or ? to list"
    prompt = "╭─gnet\n╰─➤ "
    colorama.init()

    def __init__(self):
        super().__init__()
        # To remove built-in commands entirely, delete
        # the "do_*" function from the cmd2.Cmd class
        del cmd2.Cmd.do_edit
        del cmd2.Cmd.do_history
        del cmd2.Cmd.do_shell
        del cmd2.Cmd.do_run_script
        del cmd2.Cmd.do_alias
        del cmd2.Cmd.do_set
        del cmd2.Cmd.do_run_pyscript
        del cmd2.Cmd.do_shortcuts
        del cmd2.Cmd.do_macro
        self.max_attempts = 3  # Set the maximum number of login attempts
        self.attempts = 0  # Initialize the attempt counter
        self.warnings = 0  # Initialize the warning counter
        self.debug = True  # Set debug to True by default
        self.logged_in = False

    def preloop(self):
        """Called before the command loop starts.

        Authenticates the user before entering the command loop.
        """
        self.authenticate()

    def authenticate(self):
        """Authenticates the user.

        Prompts the user for a username and password, 
        and checks them against the configured admin credentials.
        """
        GreenNetCMD.clear_screen(self)
        print("Welcome...\n\nPlease enter your credentials")
        while self.attempts < self.max_attempts:
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            if not self.check_credentials(username, password):
                GreenNetCMD.clear_screen(self)
                print("ERROR: Authentication failed\n")
                self.attempts += 1
                self.warnings += 1
                if self.attempts < self.max_attempts:
                    print(f"🚫 WARNING...! Attempt {self.attempts} of {self.max_attempts} attempts used.")
            else:
                GreenNetCMD.clear_screen(self)
                print(f"\nAccess granted\nLogged in as: [{username}]")
                self.attempts = 0
                self.warnings = 0
                return
        print("\nMaximum authentication attempts exceeded.\nExiting now...\n")
        exit(1)

    def check_credentials(self, username, password):
        """Checks the user credentials.
        
        Checks the provided credentials against 
        the configured admin credentials.

        Args:
            username (str): The provided username.
            password (str): The provided password.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        gnetadmin_user = Config.ADMIN_USERNAME
        gnetadmin_pass = Config.ADMIN_PASSWORD
        return gnetadmin_user == username and gnetadmin_pass == password

    def do_login(self, line):
        """Login to the system.

        Example:
            login
        """
        if self.logged_in:
            print("You are already logged in. Please logout first.")
            return
        GreenNetCMD.clear_screen(self)
        GreenNetCMD.authenticate(self)
        self.enable_command('exit')
        self.enable_command('quit')
        self.enable_command('logout')
        self.enable_command('help')
        self.logged_in = True
        print("Login successful")
        print(self.intro)
        self.prompt = "╭─gnet\n╰─➤ "

    def do_logout(self, line):
        """Logout from the console"""
        if not self.logged_in:
            print("You are not logged in.")
            return
        self.logged_in = False
        self.authenticate = False
        self.disable_command('exit', "Cannot exit, login first")
        self.disable_command('quit', "Cannot quit, login first")
        self.disable_command('help', "Sorry, no help at this point")
        line = None
        GreenNetCMD.clear_screen(self)
        print('Logged out successfully')
        self.prompt = '\n🔐 (Locked) '

    def do_create(self, arg):
        """Creates a new user."""
        args = arg.split()
        if len(args) != 3:
            print("Usage: create <username> <password> <email>")
            return
        username, password, email = args

        # Validate user input
        if not self.validate_username(username):
            print("Invalid username. Please use only alphanumeric characters and underscores.")
            return
        if not self.validate_password(password):
            print("Invalid password. Please use a strong password with at least 12 characters.")
            return
        if not self.validate_email(email):
            print("Invalid email address.")
            return

        # Create a new user object
        user = User(username=username, email=email)
        user.set_password(password)

        # Add the user to the database
        db.session.add(user)
        try:
            db.session.commit()
            print(f"User [{username}] created successfully")
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user")
            print(f'User: [{username}] already exists')
    
    def validate_username(self, username):
        # Validate username using a regular expression
        import re
        pattern = r'^[a-zA-Z0-9_]+$'
        if re.match(pattern, username):
            return True
        return False

    def validate_password(self, password):
        # Validate password using a regular expression
        import re
        pattern = r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=-{};:"<>,./?]).{12,}$'
        if re.match(pattern, password):
            return True
        return False

    def validate_email(self, email):
        # Validate email using a regular expression
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        return False

    def do_list(self, arg):
        users = db.session.query(User).all()
        if not users:
            print("No users found.")
        else:
            for user in users:
                print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    
    def do_get(self, arg):
        try:
            user_id = int(arg)
            user = db.session.get(User, user_id)
            if user:
                print(f"ID: {user.id}, UID: {user.uid}, Username: {user.username}, Email: {user.email}")
            else:
                print("User not found")
        except ValueError:
            print("Invalid user ID")

    def do_update(self, arg):
        args = arg.split()
        if len(args)!= 4:
            print("Usage: update <user_id> <username> <password> <email>")
            return
        user_id, username, password, email = args
        try:
            user_id = int(user_id)
            user = db.session.get(User, user_id)
            if user:
                user.username = username
                user.set_password(password)
                user.email = email
                db.session.commit()
                print(f"Updated User: <{username}>.")
            else:
                print("User not found")
        except ValueError:
            print("Invalid user ID")

    def do_update_username(self, arg):
        try:
            user_id, new_username = arg.split()
            user_id = int(user_id)
            user = db.session.get(User, user_id)
            if user:
                user.username = new_username
                db.session.commit()
                print(f"Username updated for user ID {user_id} to {new_username}")
            else:
                print("User not found")
        except ValueError:
            print("Invalid input. Please provide user ID and new username separated by a space.")

    def do_delete(self, arg):
        try:
            user_id = int(arg)
            user = db.session.get(User, user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                print(f"Deleted User: <{user.username}>.")
            else:
                print("User not found")
        except ValueError:
            print("Invalid user ID")

    def emptyline(self):
        """Called when an empty line is entered
        
        Do nothing upon receiving an empty line.
        """
        pass

    def clear_screen(self):
        """Colorama screen cleaner"""
        print(colorama.ansi.clear_screen())

    def do_clear(self, arg):
        """Clear the screen"""
        GreenNetCMD.clear_screen(self)

    def do_quit(self, arg):
        """EOF signal to exit the program."""
        GreenNetCMD.clear_screen(self)
        print("EOF reached\n")
        return True
    
    def do_exit(self, line):
        """Exit the program"""
        GreenNetCMD.do_logout(self, line)  # Logout and exit method
        line = None
        print("Thank you. Bye\n")
        return True
    
if __name__ == "__main__":
    GreenNetCMD().cmdloop()
