#!/usr/bin/python3
"""
Module defines a test for `State` class.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test `State` class"""

    def setUp(self):
        """Setup test environment"""
        self.state = State()

    def test_empty_class_attributes(self):
        """Test empty class attributes"""
        self.assertEqual(self.state.name, "")

    def test_class_attributes_type(self):
        """Test type of class attributes"""
        self.assertIsInstance(self.state.name, str)

    def test_state_inherits_from_base_model(self):
        """Test inherits from `BaseModel`class"""
        self.assertIsInstance(self.state, BaseModel)
