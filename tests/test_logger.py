# Copyright 2022 Frankie Homewood

import pytest
from pathlib import Path
import shutil

from terminal_character_sheet.logger import LoggingUtil


def test_logging_util_initializes_path_object():
    file_path = (Path(__file__).parent / "log/test_logging_util_initializes_path_object.log")
    file_path.unlink(missing_ok=True)
    logger = LoggingUtil(file_path)
    assert hasattr(logger, "directory")
    assert file_path.exists()


def test_log_prints_to_file():
    file_path = Path(__file__).parent / "log/test_log_prints_to_file.log"
    file_path.unlink(missing_ok=True)
    logger = LoggingUtil(file_path)

    logger.log("test")

    with open(file_path) as file:
        file_contents = ''.join(file.readlines())

    assert "test" in file_contents


def test_separate_log_call_append_to_file():
    file_path = Path(__file__).parent / "log/test_separate_log_call_append_to_file.log"
    file_path.unlink(missing_ok=True)
    logger = LoggingUtil(file_path)

    logger.log("test one")

    logger.log("test two")

    with open(file_path) as file:
        file_contents = ''.join(file.readlines())

    assert "test one" in file_contents
    assert "test two" in file_contents


def test_log_level_defaults_to_info():
    file_path = Path(__file__).parent / "log/test_log_level_defaults_to_info.log"
    file_path.unlink(missing_ok=True)
    logger = LoggingUtil(file_path)

    logger.log("test")

    with open(file_path) as file:
        file_contents = ''.join(file.readlines())

    assert "INFO | test" in file_contents


def test_different_levels_register_correctly():
    file_path = Path(__file__).parent / "log/test_different_levels_register_correctly.log"
    file_path.unlink(missing_ok=True)
    logger = LoggingUtil(file_path)

    logger.log("test one", level="INFO")

    logger.log("test two", level="DEBUG")

    with open(file_path) as file:
        file_contents = ''.join(file.readlines())

    assert "INFO | test one" in file_contents
    assert "DEBUG | test two" in file_contents
