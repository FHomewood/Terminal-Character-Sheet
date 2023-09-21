# Copyright 2022 Frankie Homewood

import curses
from pathlib import Path

from terminal_character_sheet import *
from terminal_character_sheet.logger import LoggingUtil


class Context:
    def __init__(self, character=None):
        self.stdscr = None
        self.character = character
        self.mouse_available = False
        self.mouse_state = (0, 0, 0, 0, 0)
        self.feature_box_keys = []
        self.modules = {}
        self.util = LoggingUtil(Path(__file__).parent.parent / 'history.log')

    def get_current_feature(self):
        current_dict = self.character.features
        for i in self.feature_box_keys:
            current_dict = current_dict[i]
        return current_dict

    def getch(self):
        key = self.stdscr.getch()
        if key == curses.KEY_MOUSE:
            old_mouse_state = list(self.mouse_state)
            new_mouse_state = list(curses.getmouse())
            for attribute in range(len(new_mouse_state)):
                if new_mouse_state[attribute] < 0:
                    new_mouse_state[attribute] = old_mouse_state[attribute]
            self.mouse_state = tuple(new_mouse_state)
        return key


class Character:
    def __init__(self, init=None, update=None, end=None):
        self.context = Context(self)

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
                self.context.stdscr.refresh()
                update(self.context)
                for function in self.update:
                    function(self.context)
                draw(self.context)

                key = self.context.getch()
                if key == ord('q'):
                    break

        except Exception as e:
            end(self.context)
            for function in self.end:
                function(self.context)
            self.context.util.log(f'An exception occurred: {e}', 'ERROR')
            raise e
        end(self.context)
        for function in self.end:
            function(self.context)

    def add_function(self, function, trigger):
        if trigger == "before":
            self.add_init(function)
        elif trigger == "during":
            self.add_update(function)
        elif trigger == "after":
            self.add_end(function)
        else:
            self.context.util.log(
                f"""Function call to Character.add_function() with invalid trigger provided
TRIGGER PROVIDED: "{trigger}" """
            )

    def add_init(self, function):
        self.init.append(function)

    def add_update(self, function):
        self.update.append(function)

    def add_end(self, function):
        self.end.append(function)

    def add_string(self, key, string, loc=(0, 0)):
        module = self.context.modules[key]
        module.var_array.append([module.pos[0] + loc[1], module.pos[1] + loc[0], str(string)])

    def add_module(self):
        pass

    def enable_dynamic_features(self):
        self.add_update(features_box_update)


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

    for identifier, block in context.modules.items():
        if block.mouse_in_block(context) and \
                block.active and \
                block.function:
            block.function(context)


def draw(context):
    for identifier, block in context.modules.items():
        block.draw(context)
    context.stdscr.addstr(0, 0, str(f"mouse: {context.mouse_available}, " \
                                    + f"y:{context.mouse_state[2]}, " \
                                    + f"x:{context.mouse_state[1]} || " \
                                    + f"{mouse_event(context)}")
                          )


def features_box_update(context):
    for i in range(16):
        headings = list(context.get_current_feature().keys())
        if not context.feature_box_keys:
            title_text = "~ Features ~"
        else:
            title_text = f'~ {context.feature_box_keys[-1]} ~'
        context.modules["Features Box"].var_array = [[31, 61 - len(title_text) // 2, title_text]]
        scroll_offset = context.modules["Features Box"].scroll

        if len(headings) > i + scroll_offset:
            context.modules[f'Features Line {i}'].var_array = [[32 + i, 44, f'{headings[i + scroll_offset]}']]
        else:
            context.modules[f'Features Line {i}'].var_array = [[0, 0, '']]


def end(context):
    curses.nocbreak()
    context.stdscr.keypad(False)
    curses.echo()
    curses.endwin()
