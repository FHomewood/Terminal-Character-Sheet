# Copyright 2022 Frankie Homewood

import pytest
from unittest.mock import patch

from terminal_character_sheet.display import Display
from terminal_character_sheet.display_module import DisplayModule


def test_display_initializes_sub_systems():
    display = Display()

    assert hasattr(display, "stdscr")
    assert hasattr(display, "mouse_state")
    assert hasattr(display, "mouse_position")
    assert hasattr(display, "mouse_button")
    assert hasattr(display, "modules")


def test_mouse_position_property():
    display = Display()
    display.mouse_state = (0, 1, 2, 3, 4)

    assert display.mouse_position == (1, 2)


def test_mouse_button_property():
    display = Display()

    display.mouse_state = (0, 1, 2, 3, 4)

    assert display.mouse_button == "Left Click"


def test_module_is_added_on_call():
    display = Display()
    test_module = DisplayModule()

    display.add_module("test_module", test_module)

    assert "test_module" in display.modules
    assert display.modules.get("test_module") == test_module


def test_module_is_removed_on_call():
    display = Display()
    display.modules = {"test_module": DisplayModule()}

    display.del_module("test_module")

    assert display.modules == {}
