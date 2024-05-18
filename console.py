#!/usr/bin/python3

import cmd
import sys
from models import storage
from models.user import User
from models.base_model import BaseModel

"""
Defines a program `console` that contains the entry point of the command
interpreter.
"""

# define global class dict
cls_dict = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """
    Defines the command interpreter
    """
    # display prompt in interactive and non-interactive mode
    if sys.stdin.isatty():
        prompt = "(hbnb) "
    else:
        prompt = "(hbnb)\n"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, save it (to JSON file)
        and prints the id
        """
        # get class name
        cls = cls_dict.get(arg)

        # validate input
        if not arg:
            print("** class name missing **")
        elif cls is None:
            print("** class doesn't exist **")
        else:
            obj = cls()  # create instance
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        args = line.split()
        if len(args) != 0:
            if len(args) == 2:
                cls = cls_dict.get(args[0])
                if cls:
                    objs = storage.all()
                    # create key
                    obj_key = "{}.{}".format(args[0], args[1])
                    if obj_key in objs:
                        obj = objs.get(obj_key)
                        print(str(obj))
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file)
        """
        args = line.split()
        if len(args) != 0:
            if len(args) == 2:
                cls = cls_dict.get(args[0])
                if cls:
                    objs = storage.all()
                    obj_key = "{}.{}".format(args[0], args[1])
                    if obj_key in objs:
                        del objs[obj_key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name
        """
        objs = storage.all()
        objs_list = []
        if arg:
            # print object of the class provided
            cls = cls_dict.get(arg)
            if cls:
                for key, obj in objs.items():
                    cls_name = key.split('.')[0]
                    if arg == cls_name:
                        objs_list.append(str(obj))
                print(objs_list)
            else:
                print("** class doesn't exist **")
        else:
            # print all objects
            for obj in objs.values():
                objs_list.append(str(obj))
            print(objs_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file
        """
        args = line.split()
        if len(args) >= 4:
            cls = cls_dict.get(args[0])
            if cls:
                objs = storage.all()
                obj_key = "{}.{}".format(args[0], args[1])
                if obj_key in objs:
                    obj = objs.get(obj_key)

                    # convert attribute_value to correct data type
                    try:
                        value = float(args[3])
                        if value.is_integer():
                            attr_value = int(value)
                        else:
                            attr_value = value
                    except ValueError:
                        # remove quotes
                        value = args[3].strip('\'"')
                        attr_value = str(value)

                    # update object
                    setattr(obj, args[2], attr_value)
                    
                    # save update to file
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            if len(args) == 0:
                print("** class name missing **")
            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                print("** attribute name missing **")
            if len(args) == 3:
                print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
