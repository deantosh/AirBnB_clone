#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel

"""
Module defines a test for `City` class
"""


class TestCity(unittest.TestCase):
    """Test `City` class"""

    def setUp(self):
        """Setup test environment"""
        self.city = City()

    def test_empty_attributes(self):
        """Test empty instance"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_non_empty_attribute(self):
        """Test the type of instance attributes"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_inherits_from_base_model(self):
        """Test inherits from `BaseModel` class"""
        self.assertIsInstance(self.city, BaseModel)
