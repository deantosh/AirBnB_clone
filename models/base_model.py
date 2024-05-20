#!/usr/bin/python3

import uuid
from datetime import datetime

"""
Module defines `BaseModel` class, that is the bases for all other classes.
"""


class BaseModel:
    """defines the base model for all classes"""

    storage = None

    def __init__(self, *args, **kwargs):
        """
        initialize the class
        """
        if BaseModel.storage is None:
            from models import storage  # lazy import
            BaseModel.storage = storage
        # If kwargs is provided (recreate object)
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            # Default initialization (new instance)

            # Generate UUID
            unique_id = uuid.uuid4()

            self.id = str(unique_id)
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

            # save new object
            BaseModel.storage.new(self)

    def __str__(self):
        """
        returns: informal string representation of object
        """
        obj_str = "[{}] ({}) {}".format(
                       type(self).__name__, self.id, self.__dict__)
        return obj_str

    def save(self):
        """
        updates the time an object has been updated
        """
        self.updated_at = datetime.utcnow()

        # save to FileStorage
        BaseModel.storage.save()

    def to_dict(self):
        """
        returns: dictionary containing all key/values of __dict__ of the
                 instance.
        """
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                obj_dict[key] = datetime.isoformat(value)
            else:
                obj_dict[key] = value
        obj_dict["__class__"] = type(self).__name__

        return obj_dict
