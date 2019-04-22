import os
from .simple_file.simple_file_data import SimpleFileData
from .without_data_file.without_data_file import WithoutDataFile
import json


class TestDataInterface(object):
    def __init__(self):
        self._setup_base_path()
        self._setup_target_path()
        self._setup_files()

    def _setup_base_path(self):
        self.base_path = os.path.join(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__))))
    
    def _setup_target_path(self):
        self.target_path = os.path.join(self.base_path, "target_data")
    
    def _setup_files(self):
        with open(os.path.join(self.base_path, 'files.json')) as f:
            files = json.load(f)['files']
            for key in files.keys():
                setattr(self, key, files[key])
        pass
        
    def getFileData(self, fileName):
        return {
            self.SIMPLE_FILE_DATA: SimpleFileData(self.base_path),
            self.WITHOUT_DATA_FILE_DATA: WithoutDataFile(self.base_path),
        }[fileName]
