import os
from .simple_file.simple_file_data import SimpleFileData
from .without_data_file.without_data_file import WithoutDataFile

class TestDataInterface(object):

    def __init__(self):
        self.base_path = os.path.join(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__))))
        self.target_path = os.path.join(self.base_path, "target_data")
        self.SIMPLE_FILE_DATA = 'simple_file'
        self.WITHOUT_DATA_FILE_DATA = 'without_data'
        pass

    def getFileData(self, fileName):
        return {
            self.SIMPLE_FILE_DATA: SimpleFileData(self.base_path),
            self.WITHOUT_DATA_FILE_DATA: WithoutDataFile(self.base_path),
        }[fileName]