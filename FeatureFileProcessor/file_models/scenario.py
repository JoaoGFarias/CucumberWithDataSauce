import re

class Scenario(object):

    def __init__(self, scenario):
        self.scenario = scenario
        self.csv = re.findall('{!(.*)!}', self.scenario[0])[0]

    def __eq__(self, other):
        return self.scenario == other
    
    def data_file(self):
        #TODO - Raise exception when there is no data file
        return self.csv
        