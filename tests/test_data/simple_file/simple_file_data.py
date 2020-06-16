import os
from ..file_data import FileData


class SimpleFileData(FileData):
    def __init__(self, base_path):
        dir_name = os.path.dirname(__file__)
        FileData.__init__(self, base_path, dir_name, 'simple_file')

    @classmethod
    def name(self):
        return "simple_file.feature"

    @classmethod
    def number_of_scenarios(self):
        return 2

    @classmethod
    def csv_file(self, scenario_number):
        return {
            1: "scenario_1_file",
            2: "scenario_2_file"
        }[scenario_number]

    @classmethod
    def feature_title(self):
        return 'Feature: Serve coffee'

    def first_scenario(self):
        return [
            "Scenario: Buy last coffee" +
            self.data_mark_at_scenario(scenario_number=1),
            "Given there are 1 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"]

    @classmethod
    def first_scenario_expected_outline(self):
        return [
            ["button_label", "coffe_label"],
            ["First Button Label", "First Coffee Label"],
            ["Second Button Label", "Second Coffee Label"]
        ]

    def first_scenario_printable_table(self):
        return self.scenario_text(1) + ["Examples:"] + ["|\tbutton_label\t|\tcoffe_label\t|"] + ["|\tFirst Button Label\t|\tFirst Coffee Label\t|"] + ["|\tSecond Button Label\t|\tSecond Coffee Label\t|"]

    def second_scenario(self):
        return [
            "Scenario: Buy first coffee " +
            self.data_mark_at_scenario(scenario_number=2),
            "Given there are 2 coffees left in the machine",
            "And I have deposited 1$",
            "When I press the coffee button",
            "Then I should be served a coffee"]

    def scenario_text(self, scenario_position):
        return {
            1: self.first_scenario(),
            2: self.second_scenario()
        }[scenario_position]

    def outline_text(self, scenario_position):
        return {
            1: self.first_scenario_expected_outline(),
        }[scenario_position]

    def printable_table_text(self, scenario_position):
        return {
            1: self.first_scenario_printable_table(),
        }[scenario_position]

    def data_mark_at_scenario(self, scenario_number):
        return self.data_file_mark().substitute(
            file=self.csv_file(scenario_number))
