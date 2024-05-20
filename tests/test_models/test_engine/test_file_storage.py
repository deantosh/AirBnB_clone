#!/usr/bin/python3
"""
Module defines a test for `FileStorage` class
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Tests `FileStorage` class
    """

    def setUp(self):
        """Setup test environment"""
        self.storage = FileStorage()
        self.objects = self.storage._FileStorage__objects
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up test environment"""

        # Delete file after use
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Clear objects
        self.objects.clear()

    def test_all_method(self):
        """Test `all` method of FileStorage"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage.all(), self.objects)

    def test_new_method(self):
        """Test `new` method of FileStorage"""
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_method(self):
        """Test `save` method of FileStorage"""
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, 'r') as file:
            data = json.load(file)

        self.assertIn(key, data)
        self.assertEqual(data[key]['__class__'], 'BaseModel')
        self.assertEqual(data[key]['id'], obj.id)

    def test_reload_method(self):
        """Test `reload` method of FileStorage"""
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        # clear __objects to reload the created object
        self.objects.clear()
        self.storage.reload()

        reloaded_obj = self.storage.all()[key]

        self.assertIn(key, self.storage.all())
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.id, obj.id)
