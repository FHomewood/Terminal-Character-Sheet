# Copyright 2022 Frankie Homewood

import pytest

from terminal_character_sheet.display_module import DisplayModule


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


def test_set_module_ascii_raises_error_on_invalid_input():
    module = DisplayModule()

    with pytest.raises(SystemError):
        module = module.set_ascii()
