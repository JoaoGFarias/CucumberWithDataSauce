import re
import os
import csv
import copy

from ..exceptions.no_data_file_exception import NoDataFileException


class Scenario(object):

    def __init__(self, scenario, data_path):
        self.scenario_text = scenario
        self.csv = re.findall('{!(.*)!}', self.scenario_text[0])
        self.data_path = data_path

    def __eq__(self, other):
        return self.scenario_text == other

    def data_file(self):
        try:
            return self.csv[0]
        except IndexError:
            raise NoDataFileException

    def outline(self):
        file_name = self.data_file() + ".csv"
        file_path = os.path.join(self.data_path, file_name)
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            return list(reader)

    def printable_scenario(self):
        try:
            scenario_outline = self.outline()
        except NoDataFileException:
            return copy.deepcopy(self.scenario_text)

        rows = ["Examples:"]
        for row in scenario_outline:
            rows.append("|\t" + '\t|\t'.join(row) + "\t|")

        return self.scenario_text + rows
