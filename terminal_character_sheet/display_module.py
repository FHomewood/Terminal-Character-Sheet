# Copyright 2022 Frankie Homewood

from terminal_character_sheet.screen import Screen

class DisplayModule:
    """Holds a module interactive module for the terminal display"""

    def __init__(self):
        self.ascii = str()
        self.position = (0, 0,)
        self.layer = int()
        self.color = None
        self.is_active = False
        self.active_color = None

    def set_ascii(self, **kwargs):
        if art:= kwargs.get("art"):
            self.ascii = art
        elif filepath:= kwargs.get("filepath"):
            self.ascii = filepath
        else:
            raise SystemError

        return self
