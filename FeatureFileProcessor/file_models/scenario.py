import re
from ..exceptions.no_data_file_exception import NoDataFileException

class Scenario(object):

    def __init__(self, scenario):
        self.scenario = scenario
        self.csv = re.findall('{!(.*)!}', self.scenario[0])

    def __eq__(self, other):
        return self.scenario == other
    
    def data_file(self):
        try:
            return self.csv[0]
        except IndexError as e:
            raise NoDataFileException
            pass
        