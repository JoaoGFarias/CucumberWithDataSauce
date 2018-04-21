import shutil
import os
from pathlib import Path


class FolderProcessor(object):

    def __init__(self, target_folder, data_folder):
        self.target_folder = target_folder
        self.data_folder = data_folder

    def prepare_target_folder(self):
        try:
            shutil.rmtree(self.target_folder)
        except FileNotFoundError as e:
            pass
        os.makedirs(self.target_folder)
        pass

    def process_data_folder(self):
        for path in Path(self.data_folder).glob('**/*.feature'):
            try:
                shutil.copy(path, self.target_folder)
            except shutil.SameFileError as e:
                continue
        pass
