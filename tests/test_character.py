# Copyright 2022 Frankie Homewood

import pytest

import terminal_character_sheet as tcs


def test_character_initializes_sub_systems():
    character = tcs.Character()

    inventory = getattr(character, "inventory")
    traits = getattr(character, "traits")
    actions = getattr(character, "actions")
    display = getattr(character, "display")
    input_handler = getattr(character, "input_handler")


def test_character_creates_inventory_instance():
    character = tcs.Character()
    assert type(getattr(character, "inventory")) == type(tcs.Inventory())

def test_character_creates_traits_instance():
    character = tcs.Character()
    assert type(getattr(character, "traits")) == type(tcs.Traits())

def test_character_creates_actions_instance():
    character = tcs.Character()
    assert type(getattr(character, "actions")) == type(tcs.Actions())

def test_character_creates_display_instance():
    character = tcs.Character()
    assert type(getattr(character, "display")) == type(tcs.Display())

def test_character_creates_input_handler_instance():
    character = tcs.Character()
    assert type(getattr(character, "input_handler")) == type(tcs.InputHandler())
