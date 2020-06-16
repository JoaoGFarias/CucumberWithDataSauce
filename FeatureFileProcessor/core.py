# -*- coding: utf-8 -*-
import os
from .file_models.feature_file import FeatureFile


class FeatureFileProcessor(object):

    def __init__(self, base_path):
        self.base_path = base_path
        self.feature_file = None

    def read_file(self, file_path):
        with open(os.path.join(self.base_path, file_path)) as file:
            return [line.strip() for line in file.read().splitlines() if line]

    def parsed_feature(self):
        return self.feature_file

    def create_scenarios(self, text, file_path=None):
        file_path = file_path if file_path else self.base_path
        current_scenario = []
        scenarios = []
        feature_title = ""
        for line in text:
            if self.__is_scenario(line):
                if current_scenario != []:
                    scenarios.append(current_scenario)
                current_scenario = [line]
            elif self.__is_feature(line):
                feature_title = line
            else:
                # It is a step
                current_scenario.append(line)
        scenarios.append(current_scenario)
        self.feature_file = FeatureFile(
            title=feature_title,
            file_scenarios=scenarios,
            data_path=file_path)
        return self.feature_file

    @classmethod
    def __is_scenario(self, line):
        return line.startswith("Scenario:")

    @classmethod
    def __is_feature(self, line):
        return line.startswith("Feature:")
