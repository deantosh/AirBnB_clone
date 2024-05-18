#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel

"""
Module defines tests for the `State` class.
"""


class TestState(unittest.TestCase):
    """Test `State` class"""

    def setUp(self):
        """Setup test environment"""
        self.state = State()

    def test_state_empty_attributes(self):
        """Test empty state object"""
        self.assertEqual(self.state.name, "")

    def test_state_value_attribute(self):
        """Test non-empty state object"""
        self.state.name = "Texas"

        self.assertEqual(self.state.name, "Texas")
        self.assertIsInstance(self.state.name, str)

    def test_state_inherits_from_base_model(self):
        """Test inherits from `BaseModel`class"""
        self.assertIsInstance(self.state, BaseModel)
