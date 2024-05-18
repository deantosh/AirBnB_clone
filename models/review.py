#!/usr/bin/python3

from models.base_model import BaseModel

"""
Module defines `Review` class -- a blueprint to create review objects
"""


class Review(BaseModel):
    """defines `Review` class"""
    place_id = ""
    user_id = ""
    text = ""
