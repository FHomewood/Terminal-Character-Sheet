# Copyright 2022 Frankie Homewood

import curses


class Screen:
    """Contains all the technical implementation of curses"""

    def __init__(self):
        self.stdscr = None
        self.mouse_state = (0, 0, 0, 0, 0)
        self.resolution = (1, 1)

    @property
    def mouse_position(self):
        return self.mouse_state[1:3]

    @property
    def mouse_button(self):
        code = self.mouse_state[4]

        button_reference = {
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
        }
        button_name = button_reference.get(code, str(code))
        return button_name

    def activate(self):
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        curses.resize_term(52, 82)
        avail_mask, old_mask = curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
        self.mouse_available = avail_mask
        self.stdscr.leaveok(True)
        self.stdscr.keypad(True)

        Screen.define_color()

    def deactivate(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    @staticmethod
    def define_color():
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    @classmethod
    def red(cls):
        return curses.color_pair(1)

    @classmethod
    def blue(cls):
        return curses.color_pair(2)

    @classmethod
    def green(cls):
        return curses.color_pair(3)

    @classmethod
    def cyan(self):
        return curses.color_pair(4)

    @classmethod
    def magenta(self):
        return curses.color_pair(5)

    @classmethod
    def yellow(cls):
        return curses.color_pair(6)

    def display_module(self, module):
        pass
