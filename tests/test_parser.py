# -*- coding: utf-8 -*-

from .context import Parser
from .test_data.test_data_interface import TestDataInterface
import unittest


class ParserTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.parser = Parser()
        self.default_result = {'dummy_arg': -666}
        pass

    def setUp(self):
        pass

    def test_can_read_feature_file(self):
        self.assertEqual(self.parser.collect_arguments(), self.default_result)
        pass


if __name__ == '__main__':
    nose.run()
