# -*- coding: utf-8 -*-

from .context import FeatureFileProcessor
from .context import FeatureFile
from .context import Scenario
import os

import unittest

class FeatureFileProcessorTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        self.simple_file_path = os.path.join("test_data", "simple_file.feature")
        self.feature_title = 'Feature: Serve coffee'
        self.first_scenario = [
            "Scenario: Buy last coffee",
            "Given there are 1 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"]
        self.second_scenario = [
            "Scenario: Buy first coffee",
            "Given there are 2 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"
        ]
        self.simple_file = [self.feature_title] + self.first_scenario + self.second_scenario

    def setUp(self):
        self.file_processor = FeatureFileProcessor(self.base_path)

    def test_can_read_feature_file(self):
        returned_text = self.file_processor.read_file(self.simple_file_path)
        assert self.file_processor.file_text == self.simple_file
        assert returned_text == self.simple_file

    def test_create_scenarios_objects(self):
        self.file_processor.read_file(self.simple_file_path)
        self.file_processor.create_scenarios()
        feature_file = self.file_processor.parsed_feature()
        self.assertIsInstance(feature_file, FeatureFile)
        self.assertEqual(feature_file.feature_title(), self.feature_title)
        self.assertEqual(feature_file.number_of_scenarios(), 2)
        self.assertIsInstance(feature_file.scenario_at(1), Scenario)
        self.assertEqual(feature_file.scenario_at(1), self.first_scenario)
        self.assertIsInstance(feature_file.scenario_at(2), Scenario)
        self.assertEqual(feature_file.scenario_at(2), self.second_scenario)

if __name__ == '__main__':
    unittest.main()
