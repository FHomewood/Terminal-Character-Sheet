import TerminalCharacterSheet as tcs
from unittest import mock
import pytest


def test_package_initialization_has_necessary_attributes():
    corrin_tosscobble = tcs.Character()

    assert hasattr(corrin_tosscobble, 'context')
    assert hasattr(corrin_tosscobble, 'init')
    assert hasattr(corrin_tosscobble, 'update')
    assert hasattr(corrin_tosscobble, 'end')

def test_custom_character_init_function_stored_correctly():

    def init(context):
        context.test_attribute = "test_attribute"

    corrin_tosscobble = tcs.Character(init=init)

    corrin_tosscobble.init(corrin_tosscobble.context)

    assert corrin_tosscobble.context.test_attribute == "test_attribute"


def test_custom_character_update_function_stored_correctly():

    def update(context):
        context.test_attribute = "test_attribute"

    corrin_tosscobble = tcs.Character(update=update)

    corrin_tosscobble.update(corrin_tosscobble.context)

    assert corrin_tosscobble.context.test_attribute == "test_attribute"


def test_custom_character_end_function_stored_correctly():
    def end(context):
        context.test_attribute = "test_attribute"

    corrin_tosscobble = tcs.Character(end=end)

    corrin_tosscobble.end(corrin_tosscobble.context)

    assert corrin_tosscobble.context.test_attribute == "test_attribute"
