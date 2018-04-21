# -*- coding: utf-8 -*-
from .context import FolderProcessor
import os
import unittest
from nose2dep.core import depends
import shutil
from .test_data.test_data_interface import TestDataInterface


class FolderProcessorTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.testData = TestDataInterface()
        self.base_path = self.testData.base_path
        self.target_path = self.testData.target_path

    def setUp(self):
        self.file_processor = FolderProcessor(
            data_folder=self.base_path, target_folder=self.target_path)

    def tearDown(self):
        try:
            shutil.rmtree(self.target_path)
        except FileNotFoundError as e:
            pass

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

    @depends(before=test_prepare_target_folder)
    def test_deletes_target_folder(self):
        self.file_processor.prepare_target_folder()
        self.file_processor.delete_target_folder()
        self.assertFalse(os.path.exists(self.target_path))
