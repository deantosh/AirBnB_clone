#!/usr/bin/python3

import cmd

"""
Defines a program `console` that contains the entry point of the command
interpreter.
"""


class HBNBCommand(cmd.Cmd):
    """
    Defines the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
