#!/usr/bin/python3

from models.base_model import BaseModel

"""
Module defines `City` class -- a blueprint for creating city objects.
"""


class City(BaseModel):
    """defines `City` class"""
    state_id = ""
    name = ""
