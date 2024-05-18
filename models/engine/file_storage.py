import os
import json
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

"""
Module defines `FileStorage` class that stores all objects created
"""

# defines class name dictionary
cls_dict = {"BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    """
    Defines a class that serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns: __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        # create the obj  key
        key = "{}.{}".format(type(obj).__name__, obj.id)

        # add obj to __objects
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the json file (path: __file_path)
        """
        # create serializable __objects
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        # open file
        with open(self.__file_path, "w") as file:
            # add objects_dict to file
            json.dump(objects_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to _objects (only if the JSON file:
        __file_path) exists; otherwise, do nothing. If file does not exists,
        no exception should be raised.
        """
        # check if file exists
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        # get class name
                        cls_name = key.split('.')[0]
                        cls = cls_dict.get(cls_name)
                        if cls:
                            self.__objects[key] = cls(**value)
                except json.JSONDecodeError:
                    pass
