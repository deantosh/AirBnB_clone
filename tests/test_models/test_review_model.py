#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel

"""
Module defines a test for `Review` class.
"""


class TestReview(unittest.TestCase):
    """Test `Review` class"""

    def setUp(self):
        """Setup test environment"""
        self.review = Review()

    def test_class_attributes(self):
        """Test class attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_class_attributes_type(self):
        """Test type of class attributes"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_inherits_from_base_model(self):
        """Test inherits from the `BaseModel` class"""
        self.assertIsInstance(self.review, BaseModel)
