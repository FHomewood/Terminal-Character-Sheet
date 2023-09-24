# Copyright 2022 Frankie Homewood

class Display:
    """Controls the terminal interface when a character is displayed"""

    def __init__(self):
        self.stdscr = None
        self.mouse_state = None

    @property
    def mouse_position(self):
        return self.mouse_state[1:3]
