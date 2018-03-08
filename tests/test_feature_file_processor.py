# -*- coding: utf-8 -*-

from .context import FeatureFileProcessor
from .context import FeatureFile
from .context import Scenario
from .context import NoDataFileException
import os

from string import Template

import unittest
from nose2dep.core import depends

class FeatureFileProcessorTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base_path =  os.path.join(
            os.path.abspath(os.path.join(os.path.dirname(__file__))),
            "test_data")
        self.simple_file_path = "simple_file.feature"
        self.file_scenario_with_data_path = "file_scenario_without_data.feature"
        self.feature_title = 'Feature: Serve coffee'
        self.data_file_mark = Template("{!$file!}")
        self.first_scenario_data_file = "scenario_1_file"
        self.first_scenario = [
            "Scenario: Buy last coffee" + self.data_file_mark.substitute(file=self.first_scenario_data_file),
            "Given there are 1 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"]
        self.second_scenario_data_file = "scenario_2_file"
        self.second_scenario = [
            "Scenario: Buy first coffee " +  self.data_file_mark.substitute(file=self.second_scenario_data_file),
            "Given there are 2 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"
        ]
        self.simple_file = [self.feature_title] + self.first_scenario + self.second_scenario
        self.scenario_witout_data = [
            "Scenario: Buy last coffee",
            "Given there are 1 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"]

    def setUp(self):
        self.file_processor = FeatureFileProcessor(self.base_path)

    def test_can_read_feature_file(self):
        returned_text = self.file_processor.read_file(self.simple_file_path)
        self.assertEqual(returned_text, self.simple_file)

    @depends(before=test_can_read_feature_file)
    def test_create_scenarios_objects(self):
        text = self.file_processor.read_file(self.simple_file_path)
        self.file_processor.create_scenarios(text)
        feature_file = self.file_processor.parsed_feature()
        self.assertIsInstance(feature_file, FeatureFile)
        self.assertEqual(feature_file.feature_title(), self.feature_title)
        self.assertEqual(feature_file.number_of_scenarios(), 2)
        self.assertIsInstance(feature_file.scenario_at(1), Scenario)
        self.assertEqual(feature_file.scenario_at(1), self.first_scenario)
        self.assertEqual(feature_file.scenario_at(1).data_file(), self.first_scenario_data_file)
        self.assertIsInstance(feature_file.scenario_at(2), Scenario)
        self.assertEqual(feature_file.scenario_at(2), self.second_scenario)
        self.assertEqual(feature_file.scenario_at(2).data_file(), self.second_scenario_data_file)
    
    @depends(before=test_can_read_feature_file)
    def test_deals_with_no_data_file(self):
        text = self.file_processor.read_file(self.file_scenario_with_data_path)
        self.file_processor.create_scenarios(text)
        scenario = self.file_processor.parsed_feature().scenario_at(1)
        with self.assertRaises(NoDataFileException) as e:
            scenario.data_file()
            self.assertEqual(e.message, "No data file")
            self.assertEqual(e.errors, [])
            
    def test_reads_outline(self):
        scenario = Scenario(self.first_scenario, self.base_path)
        expected_outline = [
            ["button_label", "coffe_label"],
            ["First Button Label", "First Coffee Label"],
            ["Second Button Label", "Second Coffee Label"]
        ]

        self.assertListEqual(scenario.outline(), expected_outline)
    
    @depends(before=test_can_read_feature_file)
    def test_prints_with_data_table(self):
        printable_scenario = Scenario(self.first_scenario, self.base_path).printable_scenario()
        expected_scenario = Scenario(
            self.first_scenario + 
            ["Examples:"] + 
            ["|\tbutton_label\t|\tcoffe_label\t|"] +
            ["|\tFirst Button Label\t|\tFirst Coffee Label\t|"] +
            ["|\tSecond Button Label\t|\tSecond Coffee Label\t|"],
            self.base_path)
        self.assertEqual(expected_scenario, printable_scenario)
    
    @depends(before=test_can_read_feature_file)
    def test_prints_without_scenario_outline(self):
        scenario = Scenario(self.scenario_witout_data, self.base_path)
        printable_scenario = scenario.printable_scenario()
        self.assertEqual(scenario, printable_scenario)
        
if __name__ == '__main__':
    nose.run()
