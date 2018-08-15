import configargparse
import os


class Parser(object):

    def __init__(self):
        self.default_config_file = [os.path.join(
            os.path.dirname(__file__),
            "default_config.yaml.dist")]

    def collect_arguments(self):
        parser = configargparse.ArgParser(
            description='Dummy args',
            default_config_files=self.default_config_file)

        parser.add_argument('--dummy_arg', type=float, help='Dummy value')
        return vars(parser.parse_known_args()[0])


if __name__ == '__main__':  # pragma: no cover
    args = Parser().collectArguments()
    print(args)