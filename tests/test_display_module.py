# Copyright 2022 Frankie Homewood

import pytest

from terminal_character_sheet.display_module import DisplayModule
from tests import TEST_FILES_DIR


def test_display_module_initializes_necessary_attributes():
    module = DisplayModule()

    assert hasattr(module, "ascii")
    assert hasattr(module, "position")
    assert hasattr(module, "layer")
    assert hasattr(module, "color")
    assert hasattr(module, "is_active")
    assert hasattr(module, "active_color")


def test_set_module_ascii_art_directly():
    test_art = "test_module"

    module = DisplayModule() \
        .set_ascii(art=test_art)

    assert module.ascii == test_art


@pytest.mark.skip
def test_set_module_ascii_art_by_file():
    pass


def test_set_module_position():
    test_position = (12, 34)

    module = DisplayModule() \
        .set_position(test_position)

    assert module.position == test_position


def test_set_module_layer():
    test_layer = 5

    module = DisplayModule() \
        .set_layer(test_layer)

    assert module.layer == test_layer


def test_module_activate():
    module = DisplayModule()
    module.is_active = False

    module = module.activate()

    assert module.is_active == True


def test_module_deactivate():
    module = DisplayModule()
    module.is_active = True

    module = module.deactivate()

    assert module.is_active == False


def test_module_toggle():
    module = DisplayModule()
    expected_activity = module.is_active
    assert module.toggle().is_active == (not expected_activity)
    assert module.toggle().is_active == expected_activity


def test_set_module_ascii_raises_error_on_invalid_input():
    module = DisplayModule()

    with pytest.raises(SystemError):
        module = module.set_ascii()


@pytest.mark.skip
def test_module_can_be_imported_from_directory():
    module = DisplayModule.import_module(TEST_FILES_DIR / "reference_module")
