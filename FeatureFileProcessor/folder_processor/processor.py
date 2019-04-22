import shutil
import os
import itertools as it
from pathlib import Path


class FolderProcessor(object):

    def __init__(self, target_folder, data_folder, file_processor=None):
        self.target_folder = target_folder
        self.data_folder = data_folder
        self.file_processor = file_processor

    def prepare_target_folder(self):
        try:
            self.delete_target_folder()
        except FileNotFoundError:
            pass
        os.makedirs(self.target_folder)

    def process_data_folder(self):
        for path in list(Path(self.data_folder).glob('**/*.feature')):
            parsed_file = self.process_file(path).feature_file_as_text()
            target_file_path = self.discover_target_file_path(path)
            Path.mkdir(target_file_path.parent, parents=True, exist_ok=True)
            with open(target_file_path, "w+") as text_file:
                text_file.write(parsed_file)

    def process_file(self, file_path):
        text = self.file_processor.read_file(file_path)
        self.file_processor.create_scenarios(text, file_path.parent)
        return self.file_processor.parsed_feature()

    def discover_target_file_path(self, path):
        path_parts = path.parts
        data_folder_parts = Path(self.data_folder).parts
        internal_file_path = [
            x for x, y
            in it.zip_longest(path_parts, data_folder_parts)
            if x != y and x is not None]
        result = Path(self.target_folder)
        for folder in internal_file_path:
            result = result.joinpath(folder)
        return result

    def delete_target_folder(self):
        shutil.rmtree(self.target_folder)
