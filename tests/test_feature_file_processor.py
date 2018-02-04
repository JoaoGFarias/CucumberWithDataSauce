# -*- coding: utf-8 -*-

from .context import FeatureFileProcessor
import sys
import os

import unittest

class FeatureFileProcessorTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        self.simple_file_path = os.path.join("test_data", "simple_file.feature")
        self.simple_file = [
            "Feature: Serve coffee",
            "Scenario: Buy last coffee",
            "Given there are 1 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"]

    def setUp(self):
        self.file_processor = FeatureFileProcessor(self.base_path)

    def test_can_read_feature_file(self):
        returned_text = self.file_processor.read_file(self.simple_file_path)
        assert self.file_processor.file_text == self.simple_file
        assert returned_text == self.simple_file

if __name__ == '__main__':
    unittest.main()