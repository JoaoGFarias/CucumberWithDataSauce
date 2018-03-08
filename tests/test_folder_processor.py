# -*- coding: utf-8 -*-
from .context import FolderProcessor
import os
import unittest
from nose2dep.core import depends
import shutil

class FolderProcessorTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.base_path = os.path.join(
            os.path.abspath(os.path.join(os.path.dirname(__file__))),
            "test_data")
        self.target_path = os.path.join(self.base_path, "target_data")
    
    def setUp(self):
        self.file_processor = FolderProcessor(data_folder = self.base_path, target_folder = self.target_path)
    
    def tearDown(self):
        shutil.rmtree(self.target_path)

    def test_prepare_target_folder(self):
        self.file_processor.prepare_target_folder()
        self.assertTrue(os.path.exists(self.target_path))
        self.assertTrue(os.path.isdir(self.target_path))
        self.assertEqual(os.listdir(self.target_path), [])
    
    @depends(before=test_prepare_target_folder)
    def test_data_flow(self):
        self.file_processor.prepare_target_folder()
        self.file_processor.process_data_folder()
        self.assertEqual(len(os.listdir(self.target_path)), 2)
        