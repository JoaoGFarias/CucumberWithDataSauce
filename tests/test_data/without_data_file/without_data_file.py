from string import Template
from functools import reduce
import os

class WithoutDataFile(object):
    def __init__(self, base_path):
        self.base_path = os.path.join(base_path, 'without_data_file')

    def name(self):
        return "file_scenario_without_data.feature"
    
    def file_path(self):
        folder_path = os.path.join(
                        os.path.abspath(
                            os.path.join(
                                os.path.dirname(__file__))))
        return os.path.join(folder_path, self.name())

    def number_of_scenarios(self):
        return 1

    def data_file_mark(self):
        return Template("{!$file!}")
    
    def feature_title(self):
        return 'Scenario: Buy last coffee'

    def first_scenario(self):
        return [
            "Scenario: Buy last coffee",
            "Given there are 1 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"]
    
    def scenario_text(self, scenario_position):
        return {
            1: self.first_scenario(),
        }[scenario_position]
    
    def feature_text(self):
        scenarios = reduce( lambda x, y: x + self.scenario_text(y) ,range(1, self.number_of_scenarios() + 1), [])
        return [self.feature_title()] + scenarios