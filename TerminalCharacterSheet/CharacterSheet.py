import curses
from pathlib import Path

from TerminalCharacterSheet import *

class Context:
    def __init__(self):
        self.stdscr = None
        self.screen_state = "character_select"
        self.mouse_state = (0, 0, 0, 0, 0)
        self.character = CharacterInformation()
        self.feature_box_keys = []
        self.modules = {}


class Character:
    def __init__(self, init=None, update=None, end=None):
        self.context = Context()
        self.init = init
        self.update = update
        self.end = end

    def Display(self):
        init(self.context)
        if self.init: self.init()
        while True:
            update(self.context)
            if self.update: self.update()
            draw(self.context)
            self.context.stdscr.refresh()

            key = self.context.stdscr.getch()
            if key == ord('q'):
                break

        end(self.context)
        if self.end: self.end()

def initialize_curses(context):
    context.stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    context.stdscr.keypad(1)
    context.stdscr.leaveok(1)
    curses.resize_term(52, 82)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)

def init(context):
    initialize_curses(context)

    define_modules()

    activate_popup(context, "")

def update(context):
    context.stdscr.clear()
    get_mouse()

    for identifier, block in config.modules.items():
        if block.mouse_in_block() and \
                block.active and \
                block.function:
            block.function()


def draw(context):
    for identifier, block in config.modules.items():
        block.draw()
    context.stdscr.addstr(0, 0,
                          str(f"y:{context.mouse_state[2]}, x:{context.mouse_state[1]} || {mouse_event()}"))


def end(context):
    curses.nocbreak()
    context.stdscr.keypad(False)
    curses.echo()
    curses.endwin()
