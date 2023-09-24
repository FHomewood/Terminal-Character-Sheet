# Copyright 2022 Frankie Homewood

from terminal_character_sheet.inventory import Inventory
from terminal_character_sheet.traits import Traits
from terminal_character_sheet.actions import Actions
from terminal_character_sheet.display import Display
from terminal_character_sheet.input_handler import InputHandler

class Character:
    """Facade Character class to communicate between different subsystems"""

    def __init__(self):
        self.display = Display()
        self.input_handler = InputHandler()

        self.traits = Traits()
        self.inventory = Inventory()
        self.actions = Actions()
