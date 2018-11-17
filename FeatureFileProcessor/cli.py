import FeatureFileProcessor
import configargparse
import os


class Parser(object):

    def __init__(self, path=None):
        if not path:
            self.default_config_file = [os.path.join(os.path.dirname(__file__),
                                                     "..",
                                                     "default_config.yaml.dist")]
        else:
            self.default_config_file = path

    def collect_arguments(self):
        parser = configargparse.ArgParser(
            description='Dummy args',
            default_config_files=self.default_config_file)

        parser.add('--dummy_arg', type=float, help='Dummy value')
        return vars(parser.parse_known_args()[0])


if __name__ == '__main__':  # pragma: no cover
    args = Parser().collect_arguments()
    text = FeatureFileProcessor(
        "D:\GitHub\PyCPD\tests\test_data\simple_file").read_file(
            self.simple_file_path)
    print(args)
    print(text)
