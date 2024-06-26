#!/usr/bin/python3
# Console for the GreenNet User Authentication System

import cmd
import os

class GreenNetCMD(cmd.Cmd):
    """Defines the GreenNet command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    intro = "\nWelcome to the GreenNet User Authentication System\nv.1.0\n"
    prompt = "╭─gnet\n╰─➤ "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == "__main__":
    GreenNetCMD().cmdloop()