class Scenario(object):

    def __init__(self, scenario):
        self.scenario = scenario

    def __eq__(self, other):
        return self.scenario == other
        