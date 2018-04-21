class NoDataFileException(Exception):

    def __init__(self, message="No data file", errors=[]):
        super().__init__(message, errors)
    pass
