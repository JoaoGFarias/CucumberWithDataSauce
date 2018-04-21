import os
from .simple_file.simple_file_data import SimpleFileData

class TestDataInterface(object):

    def __init__(self):
        self.base_path = os.path.join(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__))))
        self.target_path = os.path.join(self.base_path, "target_data")
        self.SIMPLE_FILE_DATA = 'simple_file'
        pass

    def getFileData(self, fileName):
        if fileName == self.SIMPLE_FILE_DATA:
            return SimpleFileData()