from pathlib import Path
from datetime import datetime


class LoggingUtil:
    def __init__(self, directory):
        self.directory = Path(directory)

    def log(self, contents, level='INFO'):
        with open(self.directory, 'a') as logfile:
            contents = str(contents).split('\n')
            for line in contents:
                logfile.write(f'{datetime.now()} | {level} | {line}\n')
