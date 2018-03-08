from .scenario import Scenario

class FeatureFile(object):

    def __init__(self, title, data_path, file_scenarios=[]):
        self.title = title
        self.scenarios = [Scenario(file_scenario, data_path) for file_scenario in file_scenarios]

    def feature_title(self):
        return self.title

    def number_of_scenarios(self):
        return len(self.scenarios)

    def scenario_at(self, position):
        return self.scenarios[position-1]
