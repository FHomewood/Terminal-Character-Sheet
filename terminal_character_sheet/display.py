# Copyright 2022 Frankie Homewood


from terminal_character_sheet.display_module import DisplayModule
from terminal_character_sheet.screen import Screen


class Display:
    """Controls the terminal interface when a character is displayed"""

    def __init__(self):
        self.screen = Screen()
        self.modules = {}

    def add_module(self, module_name: str, module: DisplayModule):
        self.modules[module_name] = module

    def del_module(self, module_name: str):
        if module_name in self.modules:
            self.modules.pop(module_name)
