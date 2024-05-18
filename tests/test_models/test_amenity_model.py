#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

"""
Module defines a test for `Amenity`class
"""


class TestAmenity(unittest.TestCase):
    """Test `Amenity` class"""

    def setUp(self):
        """Setup test environment"""
        self.amenity = Amenity()

    def test_empty_attributes(self):
        """Test empty instance"""
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.name, str)

    def test_inherits_from_base_model(self):
        """Test inherits from `BaseModel` class"""
        self.assertIsInstance(self.amenity, BaseModel)
