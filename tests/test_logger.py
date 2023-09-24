# Copyright 2022 Frankie Homewood

import pytest
from pathlib import Path
import shutil

from terminal_character_sheet.logger import LoggingUtil


def test_logging_util_initializes_path_object():
    file_path = Path(__file__).parent / "log/test.log"
    logger = LoggingUtil(file_path)
    assert hasattr(logger, "directory")

def test_log_prints_to_file():
    file_path = Path(__file__).parent / "log/test.log"
    shutil.rmtree(file_path.parent, ignore_errors=True)
    logger = LoggingUtil(file_path)

    logger.log("test")

    with open(file_path) as file:
        file_contents = ''.join(file.readlines())

    assert "test" in file_contents

def test_seperate_log_call_append_to_file():
    file_path = Path(__file__).parent / "log/test.log"
    shutil.rmtree(file_path.parent, ignore_errors=True)
    logger = LoggingUtil(file_path)

    logger.log("test one")

    logger.log("test two")

    with open(file_path) as file:
        file_contents = ''.join(file.readlines())

    assert "test one" in file_contents
    assert "test two" in file_contents
