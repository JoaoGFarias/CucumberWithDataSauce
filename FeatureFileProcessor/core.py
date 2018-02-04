# -*- coding: utf-8 -*-
import os

class FeatureFileProcessor(object):

    def __init__(self, base_path):
        self.base_path = base_path
        self.file_text = None

    def read_file(self, file_path):
        with open(os.path.join(self.base_path, file_path)) as file:
            self.file_text = [line.strip() for line in file.read().splitlines() if line]
        return self.file_text
