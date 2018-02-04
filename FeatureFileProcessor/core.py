# -*- coding: utf-8 -*-
import os
from .file_models.feature_file import FeatureFile

class FeatureFileProcessor(object):

    def __init__(self, base_path):
        self.base_path = base_path
        self.file_text = None
        self.scenarios = []
        self.feature_file = []
        self.feature_title = None

    def read_file(self, file_path):
        with open(os.path.join(self.base_path, file_path)) as file:
            self.file_text = [line.strip() for line in file.read().splitlines() if line]
        return self.file_text
    
    def parsed_feature(self):
        return self.feature_file

    def create_scenarios(self):
        current_scenario = []
        for line in self.file_text:
            if self.__is_scenario(line):
                if current_scenario != []:
                    self.scenarios.append(current_scenario)
                current_scenario = [line]
            elif self.__is_feature(line):
                self.feature_title = line
            else:
                # It is a step
                current_scenario.append(line)
        self.scenarios.append(current_scenario)
        self.feature_file = FeatureFile(title=self.feature_title, file_scenarios=self.scenarios)
        return self.feature_file

    def __is_scenario(self, line):
        return line.startswith("Scenario:")

    def __is_feature(self, line):
        return line.startswith("Feature:")
