import curses
from pathlib import Path

from TerminalCharacterSheet import *
from TerminalCharacterSheet.logger import LoggingUtil


class Context:
    def __init__(self):
        self.stdscr = None
        self.mouse_available = False
        self.mouse_state = (0, 0, 0, 0, 0)
        self.character = CharacterInformation()
        self.feature_box_keys = []
        self.modules = {}
        self.util = LoggingUtil(Path(__file__).parent.parent / 'history.log')


class Character:
    def __init__(self, init=None, update=None, end=None):
        self.context = Context()
        self.init = []
        if init: self.init.append(init)

        self.update = []
        if update: self.update.append(update)

        self.end = []
        if end: self.end.append(end)

    def Display(self):
        try:
            init(self.context)
            for function in self.init:
                function(self.context)
            while True:
                update(self.context)
                for function in self.update:
                    function(self.context)
                draw(self.context)
                self.context.stdscr.refresh()

                key = self.context.stdscr.getch()
                if key == ord('q'):
                    break
        finally:
            end(self.context)
            for function in self.end:
                function(self.context)

    def add_function(self, function, trigger):
        if trigger == "before": self.add_init(function)
        elif trigger == "during": self.add_update(function)
        elif trigger == "after": self.add_end(function)
        else: self.context.util.log(
            f"""Function call to Character.add_function() with invalid trigger provided
TRIGGER PROVIDED: "{trigger}" """
        )

    def add_init(self, function):
        self.init.append(function)

    def add_update(self, function):
        self.update.append(function)

    def add_end(self, function):
        self.end.append(function)


def initialize_curses(context):
    context.stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    context.stdscr.keypad(True)
    context.stdscr.leaveok(True)
    curses.resize_term(52, 82)
    avail_mask, old_mask = curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    context.mouse_available = avail_mask

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)


def init(context):
    initialize_curses(context)

    define_modules(context)


def update(context):
    context.stdscr.clear()
    if context.mouse_available:
        get_mouse(context)

    for identifier, block in context.modules.items():
        if block.mouse_in_block(context) and \
                block.active and \
                block.function:
            block.function()


def draw(context):
    for identifier, block in context.modules.items():
        block.draw(context)
    context.stdscr.addstr(0, 0, str(f"mouse: {context.mouse_available}, " \
                                  + f"y:{context.mouse_state[2]}, " \
                                  + f"x:{context.mouse_state[1]} || " \
                                  + f"{mouse_event(context)}")
                          )


def end(context):
    curses.nocbreak()
    context.stdscr.keypad(False)
    curses.echo()
    curses.endwin()
