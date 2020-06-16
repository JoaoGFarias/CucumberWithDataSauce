import os
from ..file_data import FileData


class WithoutDataFile(FileData):
    def __init__(self, base_path):
        dir_name = os.path.dirname(__file__)
        FileData.__init__(self, base_path, dir_name, 'without_data_file')

    @classmethod
    def name(self):
        return "file_scenario_without_data.feature"

    @classmethod
    def number_of_scenarios(self):
        return 1

    @classmethod
    def feature_title(self):
        return 'Scenario: Buy last coffee'

    @classmethod
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
