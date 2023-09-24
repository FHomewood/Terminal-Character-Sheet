# Copyright 2022 Frankie Homewood

import pytest
from unittest.mock import patch

from terminal_character_sheet.display import Display


def test_display_initializes_sub_systems():
    display = Display()

    assert hasattr(display, "stdscr")
    assert hasattr(display, "mouse_state")
    assert hasattr(display, "mouse_position")
    assert hasattr(display, "mouse_button")
    assert hasattr(display, "modules")


def test_mouse_position_property_calculates_correctly():
    display = Display()
    display.mouse_state = (0, 1, 2, 3, 4)

    assert display.mouse_position == (1, 2)


def test_display_getch_updates_mouse_state():
    pass


def test_display_getch_doesnt_update_negative_mouse_states():
    pass


def test_module_is_added_on_call():
    pass


def test_module_is_removed_on_call():
    pass
