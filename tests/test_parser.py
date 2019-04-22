# -*- coding: utf-8 -*-

from .context import Parser
from .test_data.test_data_interface import TestDataInterface
import unittest
import os
from pyquickhelper.pycode import skipif_travis

class ParserTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.parser = Parser()
        self.default_result = {
            'base': "PATH_TO_FEATURE_FILES",
            'target': "PATH_TO_SAVE_PARSED_FILES"}
        pass

    def setUp(self):
        pass

    def test_can_read_default_config_file(self):
        self.assertEqual(self.parser.collect_arguments(), self.default_result)
        pass

    def test_can_read_custom_config_file(self):
        path = self.custom_path()
        parser = Parser(path)

        self.assertEqual(parser.collect_arguments(), {
            'target': "~/sandbox/temp",
            'base': "/host/GitHub/PyCPD/tests/test_data"
        })
        pass

    @skipif_travis("Travis folder not located correctly")
    def test_calls_folder_processor(self):
        path = self.custom_path()
        parser = Parser(path)
        processor = parser.run()
        target_folder = "~/sandbox/temp"
        self.assertEqual(
            self.number_files_in_directory(
                target_folder),
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
