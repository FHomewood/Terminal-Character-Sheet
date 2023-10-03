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
        if art := kwargs.get("art"):
            self.ascii = art
        elif filepath := kwargs.get("filepath"):
            self.ascii = filepath
        else:
            raise SystemError
        return self

    def set_position(self, position: tuple):
        self.position = position
        return self

    def set_layer(self, layer: int):
        self.layer = layer
        return self

    def set_color(self, color: str):
        curses_color = getattr(Screen, color)
        self.color = curses_color()
        return self

    def set_active_color(self, color: str):
        curses_color = getattr(Screen, color)
        self.color = curses_color()
        return self

    def activate(self):
        self.is_active = True
        return self

    def deactivate(self):
        self.is_active = False
        return self

    def toggle(self):
        self.is_active = not self.is_active
        return self

    @staticmethod
    def import_module(directory_path):
        pass
