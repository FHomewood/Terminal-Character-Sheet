# Copyright 2022 Frankie Homewood

from terminal_character_sheet.display_module import DisplayModule


class Display:
    """Controls the terminal interface when a character is displayed"""

    def __init__(self):
        self.stdscr = None
        self.mouse_state = (0, 0, 0, 0, 0)
        self.modules = {}

    @property
    def mouse_position(self):
        return self.mouse_state[1:3]

    @property
    def mouse_button(self):
        code = self.mouse_state[4]
        return {
            0: 'None',
            1: 'Left Button Release',
            2: 'Left Button Press',
            4: 'Left Click',
            8: 'Double Left Click',
            32: 'Middle Button Release',
            64: 'Middle Button Press',
            128: 'Middle Click',
            256: 'Double Middle Click',
            1024: 'Right Button Release',
            2048: 'Right Button Press',
            4096: 'Right Click',
            8192: 'Double Right Click',
            65536: 'Scroll Up',
            2097152: 'Scroll Down',
        }.get(code, str(code))

    def add_module(self, module_name: str, module: DisplayModule):
        self.modules[module_name] = module

    def del_module(self, module_name: str):
        if module_name in self.modules:
            self.modules.pop(module_name)
