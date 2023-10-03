# Copyright 2022 Frankie Homewood

import pytest
from unittest.mock import patch

from terminal_character_sheet.screen import Screen
from terminal_character_sheet.display_module import DisplayModule


def test_screen_initializes_necessary_attributes():
    screen = Screen()

    assert hasattr(screen, "mouse_state")
    assert hasattr(screen, "mouse_position")
    assert hasattr(screen, "resolution")


def test_mouse_position_property():
    screen = Screen()
    screen.mouse_state = (0, 1, 2, 3, 4)

    assert screen.mouse_position == (1, 2)


def test_mouse_button_property():
    screen = Screen()

    screen.mouse_state = (0, 1, 2, 3, 4)

    assert screen.mouse_button == "Left Click"


@patch("curses.nocbreak")
@patch.object(Screen(), "stdscr")
@patch("curses.echo")
@patch("curses.endwin")
def test_deactivate_closes_curses_window(endwin_mock, echo_mock, stdscr_mock, cbreak_mock):
    screen = Screen()
    screen.stdscr = stdscr_mock
    screen.deactivate()

    assert endwin_mock.call_count == 1


@pytest.mark.skip
# @patch.dict("sys.modules", curses=MagicMock())
@patch("curses.initscr")
def test_activate_initializes_curses_window(initscr_mock):
    screen = Screen()
    screen.resolution = (10, 10)
    try:
        screen.activate()
    except:
        pass

    assert initscr_mock.call_count == 1


@pytest.mark.skip
def test_module_errors_on_empty_module():
    screen = Screen()
    module = DisplayModule()

    screen.display_module(module)


@pytest.mark.skip
def test_module_displays_on_screen():
    screen = Screen()
    module = DisplayModule()

    screen.display_module(module)


@pytest.mark.skip
def test_color_functions_work_after_definition():
    screen = Screen()

    screen.define_color()

    Screen.yellow()
