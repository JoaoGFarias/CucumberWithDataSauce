# -*- coding: utf-8 -*-

from .context import FeatureFileProcessor
from .context import FeatureFile
from .context import Scenario
from .context import NoDataFileException
import unittest

from .test_data.test_data_interface import TestDataInterface


class FeatureFileProcessorTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.testData = TestDataInterface()
        self.simpleFileData = self.testData.getFileData(
            self.testData.SIMPLE_FILE_DATA)
        self.base_path = self.simpleFileData.base_path
        self.withoutDataFile = self.testData.getFileData(
            self.testData.WITHOUT_DATA_FILE_DATA)
        self.scenario_witout_data = self.withoutDataFile.scenario_text(1)

    def setUp(self):
        self.file_processor = FeatureFileProcessor(self.base_path)

    def test_prints_with_data_table(self):
        printable_scenario = self.__create_scenario_at_position__(
            1).printable_scenario()
        expected_scenario = Scenario(
            self.simpleFileData.printable_table_text(1),
            self.base_path)
        self.assertEqual(expected_scenario, printable_scenario)

    def test_prints_without_scenario_outline(self):
        scenario = Scenario(self.scenario_witout_data, self.base_path)
        printable_scenario = scenario.printable_scenario()
        self.assertEqual(scenario, printable_scenario)

    def __create_scenario_at_position__(self, scenario_position):
        return Scenario(
            self.simpleFileData.scenario_text(scenario_position),
            self.base_path)


if __name__ == '__main__':
    nose.run()
