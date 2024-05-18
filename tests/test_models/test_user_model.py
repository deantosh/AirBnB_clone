#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel

"""
Module defines a test for `User` class.
"""


class TestUser(unittest.TestCase):
    """Test `User` class"""

    def setUp(self):
        """Setup test environment"""
        self.user = User()

    def test_empty_attributes(self):
        """Test an empty user object"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_non_empty_attributes(self):
        """Test user attributes with values"""

        # create user object
        self.user.email = "airbnb@mail.com"
        self.user.password = "root"
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"

        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "airbnb@mail.com")
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "root")
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "Betty")
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "Bar")

    def test_inherits_from_base_model(self):
        """Test user inherits from `BaseModel` class"""
        self.assertIsInstance(self.user, BaseModel)
