# Copyright 2022 Frankie Homewood

from terminal_character_sheet.inventory import Inventory

class Character:
    """Facade Character class to communicate between different subsystems"""

    def __init__(self):
        self.display = None
        self.input_handler = None

        self.traits = None
        self.inventory = Inventory()
        self.actions = None
