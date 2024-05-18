#!/usr/bin/python3

from models.base_model import BaseModel

"""
Module defines a class `User` that inherits from BaseModel
"""


class User(BaseModel):
    """defines a User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
