#!/usr/bin/python3
# # Console for the GreenNet User Authentication System

import os
import cmd
import datetime
import getpass
import app
from app.utils.db import db
from app.config.config import Config
# from app.models import user, notification, notification_threshold, notification_setting, notification_history, device, device_data

# app.app_context().push()

class GreenNetCMD(cmd.Cmd):
    """GreenNet User Authentication System console.

    This class provides a command-line interface for 
    interacting with the GreenNet system.
    """
    intro = "\nWelcome to the GreenNet User Authentication System\nv.1.0\n\nType help or ? to list"
    prompt = "╭─gnet\n╰─➤ "

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
        print("Welcome...\n\nPlease enter your credentials")
        self.check = True
        if self.check:
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            if not self.check_credentials(username, password):
                print("Authentication failed: invalid credentials")
                print("Exiting...")
                exit(1)
            print(f"\nAccess granted\nLogged in as: [{username}]")


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

    def emptyline(self):
        """Called when an empty line is entered
        
        Do nothing upon receiving an empty line.
        """
        pass

    def do_login(self, line):
        """Login to the system.

        Example:
            login
        """
        GreenNetCMD.authenticate(self)
        line = None
        print("Login successful")
        print(self.intro)
        self.prompt = "╭─gnet\n╰─➤ "
    
    def clear_screen(self):
        """Clear the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_logout(self, line):
        """Logout from the console"""
        self.authenticate = False
        line = None
        GreenNetCMD.clear_screen(self)
        self.prompt = '(system locked) '
        print('Logged out successfully\n')

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("EOF reached\n")
        return True
    
    def do_exit(self, line):
        """Exit the program"""
        GreenNetCMD.do_logout(self, line)
        line = None
        print("Bye bye\n")
        return True


if __name__ == "__main__":
    GreenNetCMD().cmdloop()
