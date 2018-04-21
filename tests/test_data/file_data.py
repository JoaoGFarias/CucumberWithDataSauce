import abc
import os
from string import Template
from functools import reduce


class FileData(object):
    def __init__(self, base_path, dir_name, name):
        self.base_path = os.path.join(base_path, name)
        self.dir_name = dir_name

    def file_path(self):
        folder_path = os.path.join(
            os.path.abspath(
                os.path.join(
                    self.dir_name)))
        return os.path.join(folder_path, self.name())

    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def number_of_scenarios(self):
        pass

    def data_file_mark(self):
        return Template("{!$file!}")

    @abc.abstractmethod
    def csv_file(self):
        pass

    @abc.abstractmethod
    def feature_title(self):
        pass

    @abc.abstractmethod
    def scenario_text(self, scenario_position):
        pass

    @abc.abstractmethod
    def outline_text(self, scenario_position):
        pass

    @abc.abstractmethod
    def printable_table_text(self, scenario_position):
        pass

    def feature_text(self):
        scenarios = reduce(lambda x, y: x + self.scenario_text(y),
                           range(1, self.number_of_scenarios() + 1), [])
        return [self.feature_title()] + scenarios


pass
