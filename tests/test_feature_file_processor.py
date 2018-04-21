# -*- coding: utf-8 -*-

from .context import FeatureFileProcessor
from .context import FeatureFile
from .context import Scenario
from .context import NoDataFileException
import unittest
from nose2dep.core import depends

from .test_data.test_data_interface import TestDataInterface


class FeatureFileProcessorTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.testData = TestDataInterface()
        self.simpleFileData = self.testData.getFileData(
            self.testData.SIMPLE_FILE_DATA)
        self.base_path = self.simpleFileData.base_path
        self.simple_file_path = self.simpleFileData.file_path()
        self.feature_title = self.simpleFileData.feature_title()
        self.data_file_mark = self.simpleFileData.data_file_mark()
        self.first_scenario = self.simpleFileData.first_scenario()
        self.second_scenario_data_file = self.simpleFileData.csv_file(
            scenario_number=2)
        self.second_scenario = self.simpleFileData.second_scenario()
        self.simple_file = self.simpleFileData.feature_text()
        self.withoutDataFile = self.testData.getFileData(
            self.testData.WITHOUT_DATA_FILE_DATA)
        self.scenario_witout_data = self.withoutDataFile.scenario_text(1)
        self.file_scenario_with_data_path = self.withoutDataFile.name()

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
        self.assertEqual(feature_file.number_of_scenarios(),
                         self.simpleFileData.number_of_scenarios())
        for scenario_number in range(1, self.simpleFileData.number_of_scenarios()):
            self.assertIsInstance(
                feature_file.scenario_at(scenario_number), Scenario)
            self.assertEqual(feature_file.scenario_at(
                scenario_number), self.simpleFileData.scenario_text(scenario_number))
            self.assertEqual(feature_file.scenario_at(
                scenario_number).data_file(), self.simpleFileData.csv_file(scenario_number))

    @depends(before=test_can_read_feature_file)
    def test_deals_with_no_data_file(self):
        processor = FeatureFileProcessor(self.withoutDataFile.base_path)
        text = processor.read_file(self.file_scenario_with_data_path)
        self.file_processor.create_scenarios(text)
        scenario = self.file_processor.parsed_feature().scenario_at(1)
        with self.assertRaises(NoDataFileException) as e:
            scenario.data_file()
            self.assertEqual(e.message, "No data file")
            self.assertEqual(e.errors, [])

    def test_reads_outline(self):
        scenario_position = 1
        scenario = self.__create_scenario_at_position__(scenario_position)
        expected_outline = self.simpleFileData.outline_text(scenario_position)

        self.assertListEqual(scenario.outline(), expected_outline)

    @depends(before=test_can_read_feature_file)
    def test_prints_with_data_table(self):
        printable_scenario = self.__create_scenario_at_position__(
            1).printable_scenario()
        expected_scenario = Scenario(
            self.simpleFileData.printable_table_text(1),
            self.base_path)
        self.assertEqual(expected_scenario, printable_scenario)

    @depends(before=test_can_read_feature_file)
    def test_prints_without_scenario_outline(self):
        scenario = Scenario(self.scenario_witout_data, self.base_path)
        printable_scenario = scenario.printable_scenario()
        self.assertEqual(scenario, printable_scenario)

    def __create_scenario_at_position__(self, scenario_position):
        return Scenario(self.simpleFileData.scenario_text(scenario_position), self.base_path)


if __name__ == '__main__':
    nose.run()
