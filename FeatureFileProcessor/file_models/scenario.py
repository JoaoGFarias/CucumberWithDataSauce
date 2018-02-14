import re
import os
import csv
import copy

from ..exceptions.no_data_file_exception import NoDataFileException

class Scenario(object):

    def __init__(self, scenario, data_path):
        self.scenario = scenario
        self.csv = re.findall('{!(.*)!}', self.scenario[0])
        self.data_path = data_path

    def __eq__(self, other):
        return self.scenario == other
    
    def data_file(self):
        try:
            return self.csv[0]
        except IndexError as e:
            raise NoDataFileException
    
    # TODO - Update to scenario outline
    def data_table(self):
        file_name = self.data_file()
        with open(os.path.join(self.data_path, file_name + ".csv"), newline='') as file:
            reader = csv.reader(file)
            return list(reader)

    def printable_scenario(self):
        try:
            scenario_outline = self.data_table()
        except NoDataFileException:
            return copy.deepcopy(self.scenario)
            
        rows = ["Examples:"]
        for row in scenario_outline:
            rows.append("|\t" + '\t|\t'.join(row) + "\t|")
        return self.scenario + rows