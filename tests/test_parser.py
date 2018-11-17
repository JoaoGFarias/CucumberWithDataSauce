# -*- coding: utf-8 -*-

from .context import Parser
from .test_data.test_data_interface import TestDataInterface
import unittest
import os


class ParserTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.parser = Parser()
        self.default_result = {'dummy_arg': -
                               666, 'target': None, 'base': None}
        pass

    def setUp(self):
        pass

    def test_can_read_default_config_file(self):
        self.assertEqual(self.parser.collect_arguments(), self.default_result)
        pass

    def test_can_read_custom_config_file(self):
        path = self.custom_path()
        parser = Parser(path)

        self.assertEqual(parser.collect_arguments(), {'dummy_arg': 12.0,
                                                      'target': "D:\\GitHub\\PyCPD\\temp",
                                                      'base': "D:\\GitHub\\PyCPD\\tests\\test_data"})
        pass

    def test_calls_folder_processor(self):
        path = self.custom_path()
        parser = Parser(path)
        processor = parser.run()
        self.assertEqual(
            self.number_files_in_directory(
                processor.target_folder),
            3)
        processor.delete_target_folder()
        pass

    def custom_path(self):
        return [os.path.join(os.path.dirname(__file__),
                             "test_data",
                             "custom_config.yaml")]

    def number_files_in_directory(self, target_path):
        return sum([len(files) for _, _, files in os.walk(target_path)])


if __name__ == '__main__':
    nose.run()
