# Copyright 2022 Frankie Homewood

import terminal_character_sheet as tcs
import pytest


def test_context_initialization_has_necessary_attributes():
    context = tcs.Context()

    assert hasattr(context, 'stdscr')
    assert hasattr(context, 'character')
    assert hasattr(context, 'mouse_available')
    assert hasattr(context, 'mouse_state')
    assert hasattr(context, 'feature_box_keys')
    assert hasattr(context, 'modules')
    assert hasattr(context, 'util')


def test_current_feature_function_returns_full_features_when_none_selected():
    corrin_tosscobble = tcs.Character__Reference()
    context = corrin_tosscobble.context

    corrin_tosscobble.features = {
        'Darkvision': "Can see in the dark",
        'Bardic Inspiration': "Good vibes -> Good fights"
    }

    actual = context.get_current_feature()
    expected = {
        'Darkvision': "Can see in the dark",
        'Bardic Inspiration': "Good vibes -> Good fights"
    }

    assert actual == expected


def test_current_feature_function_returns_correct_dictionary_when_keys_selected():
    corrin_tosscobble = tcs.Character__Reference()
    context = corrin_tosscobble.context

    corrin_tosscobble.features = {
        "Inventory": {
            "Weapons": "None we are pacifists",
            "Armour": "A cool hat"
        }
    }
    context.feature_box_keys = ["Inventory"]

    actual = context.get_current_feature()

    expected = {
        "Weapons": "None we are pacifists",
        "Armour": "A cool hat"
    }

    assert actual == expected
