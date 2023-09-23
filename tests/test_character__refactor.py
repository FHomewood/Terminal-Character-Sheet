# Copyright 2022 Frankie Homewood

import terminal_character_sheet as tcs
from unittest import mock
import pytest


def test_character_initialization_has_necessary_attributes():
    corrin_tosscobble = tcs.Character__Reference()

    assert hasattr(corrin_tosscobble, 'context')
    assert hasattr(corrin_tosscobble, 'init')
    assert hasattr(corrin_tosscobble, 'update')
    assert hasattr(corrin_tosscobble, 'end')

def test_custom_character_init_function_stored_correctly():

    def init(context):
        context.test_attribute = "test_attribute"

    corrin_tosscobble = tcs.Character__Reference(init=init)

    for function in corrin_tosscobble.init:
        function(corrin_tosscobble.context)

    actual = corrin_tosscobble.context.test_attribute

    expected = "test_attribute"

    assert actual == expected


def test_custom_character_update_function_stored_correctly():

    def update(context):
        context.test_attribute = "test_attribute"

    corrin_tosscobble = tcs.Character__Reference(update=update)

    for function in corrin_tosscobble.update:
        function(corrin_tosscobble.context)

    actual = corrin_tosscobble.context.test_attribute

    expected = "test_attribute"

    assert actual == expected


def test_custom_character_end_function_stored_correctly():
    def end(context):
        context.test_attribute = "test_attribute"

    corrin_tosscobble = tcs.Character__Reference(end=end)

    for function in corrin_tosscobble.end:
        function(corrin_tosscobble.context)

    actual = corrin_tosscobble.context.test_attribute

    expected = "test_attribute"

    assert actual == expected
