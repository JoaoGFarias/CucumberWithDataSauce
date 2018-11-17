# -*- coding: utf-8 -*-

from .context import Parser
from .test_data.test_data_interface import TestDataInterface
import unittest
import os


class ParserTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.parser = Parser()
        self.default_result = {'dummy_arg': -666}
        pass

    def setUp(self):
        pass

    def test_can_read_default_config_file(self):
        self.assertEqual(self.parser.collect_arguments(), self.default_result)
        pass

    def test_can_read_custom_config_file(self):
        path = [os.path.join(os.path.dirname(__file__),
                             "test_data",
                             "custom_config.yaml")]
        parser = Parser(path)
        self.assertEqual(parser.collect_arguments(), {'dummy_arg': 12})
        pass


if __name__ == '__main__':
    nose.run()
