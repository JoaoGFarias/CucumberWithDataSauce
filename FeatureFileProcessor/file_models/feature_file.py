from .scenario import Scenario
from functools import reduce


class FeatureFile(object):

    def __init__(self, title, data_path, file_scenarios=[]):
        self.title = title
        self.scenarios = [Scenario(file_scenario, data_path)
                          for file_scenario in file_scenarios]

    def feature_title(self):
        return self.title

    def number_of_scenarios(self):
        return len(self.scenarios)

    def scenario_at(self, position):
        return self.scenarios[position-1]

    def feature_file_as_text(self):
        printable_scenarios = [scenario.printable_scenario()
                               for scenario in self.scenarios]
        scenarios_as_text = ["\n" + "\n".join(scenario)
                             for scenario in printable_scenarios]
        return self.feature_title() + "\n" + "\n".join(scenarios_as_text)
