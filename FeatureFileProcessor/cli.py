from FeatureFileProcessor import FeatureFileProcessor
from .folder_processor.processor import FolderProcessor
import configargparse
import os


class Parser(object):

    def __init__(self, path=None):
        self.default_config_file = path if path else [
            os.path.join(os.path.dirname(__file__), "..", "default_config.yaml.dist")]

    def collect_arguments(self):
        args = configargparse.ArgParser(
            description='Parser arguments',
            default_config_files=self.default_config_file)
        args.add('--target', help='Folder where the processed files are stored')
        args.add('--base', help='Folder where the original files are stored')
        return vars(args.parse_known_args()[0])

    def run(self):
        args = self.collect_arguments()
        file_processor = FolderProcessor(
            data_folder=args['base'],
            target_folder=args['target'],
            file_processor=FeatureFileProcessor(args['base']))
        file_processor.prepare_target_folder()
        file_processor.process_data_folder()
        return file_processor
