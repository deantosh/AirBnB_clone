#!/usr/bin/python3
"""
Module defines a test for `Amenity`class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test `Amenity` class"""

    def setUp(self):
        """Setup test environment"""
        self.amenity = Amenity()

    def test_empty_attributes(self):
        """Test empty instance"""
        self.assertEqual(self.amenity.name, "")

    def test_type_attributes(self):
        """Test type of attributes"""
        self.assertIsInstance(self.amenity.name, str)

    def test_inherits_from_base_model(self):
        """Test inherits from `BaseModel` class"""
        self.assertIsInstance(self.amenity, BaseModel)
