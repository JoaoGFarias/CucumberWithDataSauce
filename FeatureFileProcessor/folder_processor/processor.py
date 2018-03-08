import shutil
import os

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