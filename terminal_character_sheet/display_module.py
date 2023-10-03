# Copyright 2022 Frankie Homewood


class DisplayModule:
    """Holds a module interactive module for the terminal display"""

    def __init__(self):
        self.ascii = str()
        self.position = tuple()
        self.layer = int()
        self.color = str()
        self.active_color = str()

    def set_ascii(self, **kwargs):
        art = kwargs.get("art", None)
        filepath = kwargs.get("filepath", None)

        if art:
            self.ascii = art
        elif filepath:
            self.ascii = filepath
        else:
            raise SystemError

        return self
