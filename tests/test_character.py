# Copyright 2022 Frankie Homewood

import pytest

from terminal_character_sheet.character import Character
from terminal_character_sheet.inventory import Inventory
from terminal_character_sheet.traits import Traits
from terminal_character_sheet.actions import Actions
from terminal_character_sheet.display import Display
from terminal_character_sheet.input_handler import InputHandler


def test_character_initializes_sub_systems():
    character = Character()

    assert hasattr(character, "inventory")
    assert hasattr(character, "traits")
    assert hasattr(character, "actions")
    assert hasattr(character, "display")
    assert hasattr(character, "input_handler")


def test_character_creates_inventory_instance():
    character = Character()
    assert type(getattr(character, "inventory")) == Inventory


def test_character_creates_traits_instance():
    character = Character()
    assert type(getattr(character, "traits")) == Traits


def test_character_creates_actions_instance():
    character = Character()
    assert type(getattr(character, "actions")) == Actions


def test_character_creates_display_instance():
    character = Character()
    assert type(getattr(character, "display")) == Display


def test_character_creates_input_handler_instance():
    character = Character()
    assert type(getattr(character, "input_handler")) == InputHandler
