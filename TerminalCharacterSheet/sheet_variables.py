import curses
from numpy import random
from pathlib import Path
import configparser
import re


class InteractiveBlock:

    def __init__(self, pos, color, art):
        self.render = True
        self.active = True
        self.pos = pos
        self.color = color
        self.art = art
        self.var_array = []
        self.function = None
        self.config = {}

    def replace_in_string(self, y, x, val):
        line_array = self.art.split('\n')
        pre_change = line_array[:y - 1]
        change_line = line_array[y]
        change_line = [change_line[:x] + val + change_line[x + len(val):]]
        post_change = line_array[y + 1:]
        new_string = pre_change + change_line + post_change
        new_string = '\n'.join(new_string)
        return new_string

    def draw(self, context):
        if not self.render: return
        if self.mouse_in_block(context) and self.active:
            color = self.color
        else:
            color = 0

        if 'transparent_char' in self.config.keys():
            transparent_char = self.config['transparent_char']
            x = self.pos[1]
            y = self.pos[0]
            for y_index, line, in enumerate(self.art.split('\n')):
                for x_index, character in enumerate(line):
                    if character != transparent_char:
                        context.stdscr.addstr(y + y_index, x + x_index, character, curses.color_pair(color))
        else:
            for index, line in enumerate(self.art.split('\n')):
                context.stdscr.addstr(self.pos[0] + index, self.pos[1], line, curses.color_pair(color))

        for y, x, line in self.var_array:
            context.stdscr.addstr(y, x, line, curses.color_pair(color))

    def mouse_in_block(self, context):
        t = self.pos[0]
        l = self.pos[1]
        b = t + len(self.art.split('\n'))
        r = l + max([len(line) for line in self.art.split('\n')]) - 1

        x = context.mouse_state[1]
        y = context.mouse_state[2]

        return (x >= l and x <= r and y >= t and y < b)


class Item:
    def __init__(self, name="Nothing", description="You feel a small void in your pockets where your items should be.",
                 weight="0", value="0", quantity=1):
        self.name = name
        self.description = description
        self.weight = weight
        self.value = value
        self.quantity = quantity

    def __str__(self):
        popup_text = f"""
  {self.name} x{self.quantity}

  {self.weight} lbs
  {self.value} cp
                ~~~~~~~~~~~~~~~~~
 
"""

        for line in neatify_string(self.description):
            popup_text += f" {line}\n"

        return popup_text


class Spell:
    def __init__(self,
                 name=None, description=None, school=None, level=None, cast_time=None,
                 range=None, concentration=None, ritual=None, verbal=None, somatic=None,
                 material=None, duration=None, function=None):
        self.name = name
        self.description = description
        self.school = school
        self.level = level
        self.cast_time = cast_time
        self.range = range
        self.concentration = concentration
        self.ritual = ritual
        self.verbal = verbal
        self.somatic = somatic
        self.material = material
        self.duration = duration
        self.function = function

    def __str__(self):
        popup_text = f""" 
  {self.name}
  Level {self.level} {self.school}
  
  Cast Time: {self.cast_time}
  Range: {self.range}
  Duration: {self.duration}
  {"V" * bool(self.verbal)}{"S" * bool(self.somatic)}{"M" * bool(self.material)}              {"C" * bool(self.concentration)} {"R" * bool(self.ritual)}
                ~~~~~~~~~~~~~~~~~

"""
        for line in neatify_string(self.description):
            popup_text += f" {line}\n"

        return popup_text


class InfoParser(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d


def define_modules(context):
    modules_directory = Path(__file__).parent / "modules"
    module_paths = modules_directory.glob('./*/')
    modules = {}
    for path in module_paths:
        info = InfoParser()
        info.read(path / 'module.info')
        with open(path / "module.art", 'r') as art_file:
            art = ''.join(art_file.readlines())[0:-1]
        module_info = info.as_dict()
        key = list(module_info.keys())[0]
        module_info[key]['art'] = art
        z = module_info[key]['z']
        modules[z] = module_info
    layers_dict = list(modules.keys())
    layers_dict.sort()
    for z in layers_dict:
        key = list(modules[z].keys())[0]
        module = modules[z][key]
        context.modules[key] = InteractiveBlock(
            (int(module['y']), int(module['x'])),
            int(module['active_colour']),
            module['art']
        )
        if config_keys := [key for key in list(module.keys()) if
                           key not in ['x', 'y', 'z', 'colour', 'active_colour', 'art']]:
            for config_key in config_keys:
                context.modules[key].config[config_key] = module[config_key]

    context.modules["Features Box"].scroll = 0
    context.modules["Features Line 0"].function = feature_box_select(context, 0)
    context.modules["Features Line 1"].function = feature_box_select(context, 1)
    context.modules["Features Line 2"].function = feature_box_select(context, 2)
    context.modules["Features Line 3"].function = feature_box_select(context, 3)
    context.modules["Features Line 4"].function = feature_box_select(context, 4)
    context.modules["Features Line 5"].function = feature_box_select(context, 5)
    context.modules["Features Line 6"].function = feature_box_select(context, 6)
    context.modules["Features Line 7"].function = feature_box_select(context, 7)
    context.modules["Features Line 8"].function = feature_box_select(context, 8)
    context.modules["Features Line 9"].function = feature_box_select(context, 9)
    context.modules["Features Line 10"].function = feature_box_select(context, 10)
    context.modules["Features Line 11"].function = feature_box_select(context, 11)
    context.modules["Features Line 12"].function = feature_box_select(context, 12)
    context.modules["Features Line 13"].function = feature_box_select(context, 13)
    context.modules["Features Line 14"].function = feature_box_select(context, 14)
    context.modules["Features Line 15"].function = feature_box_select(context, 15)
    context.modules["Popup"].function = popup_function
    context.modules["Popup"].scroll = 0
    context.modules["Popup"].text = ""
    context.modules["Popup"].render = False
    context.modules["Popup"].active = False


def neatify_string(string, splitlen=48):
    chunks = []
    while string != '':
        if len(string) >= splitlen:
            trial_chunk = ' '.join(string[0:splitlen].split(' ')[0:-1])
            if '\n' in trial_chunk:
                trial_chunk = trial_chunk.split('\n')[0]
            string = string[len(trial_chunk) + 1:]
        else:
            trial_chunk = string
            string = ''
        chunks.append(trial_chunk)
    return chunks


def feature_box_select(context, line_index):
    def func(context):

        current_feature = context.character.features
        for i in context.feature_box_keys:
            current_feature = current_feature[i]

        current_headings = list(current_feature.keys())
        scroll_offset = context.modules["Features Box"].scroll
        if mouse_event(context) == "Double Left Click":

            if line_index < len(current_headings) - scroll_offset:
                selected_heading = list(current_feature.keys())[line_index + scroll_offset]
                selected_attribute = current_feature[selected_heading]

                if type(selected_attribute) == dict:
                    context.feature_box_keys.append(selected_heading)
                    context.modules["Features Box"].scroll = 0

                elif type(selected_attribute) == str:
                    string = selected_attribute
                    popup_text = f""" 
   {selected_heading}
 
"""
                    for line in neatify_string(string):
                        popup_text += f" {line}\n"
                    activate_popup(context, popup_text)

                else:
                    activate_popup(context, str(selected_attribute))
        if mouse_event(context) in ["Right Click", "Double Right Click"]:
            context.feature_box_keys = context.feature_box_keys[:-1]
            context.modules["Features Box"].scroll = 0
        if mouse_event(context) == "Scroll Up":
            context.modules["Features Box"].scroll = max(0, context.modules["Features Box"].scroll - 1)
        if mouse_event(context) == "Scroll Down":
            context.modules["Features Box"].scroll = min(context.modules["Features Box"].scroll + 1,
                                                         len(current_headings) - 1)

    return func


def roll(context, n, k, b=0):
    def func(_context):
        if mouse_event(_context) == "Double Left Click":
            rv = sum([random.randint(1, k + 1) for roll_num in range(n)]) + b
            _context.modules["Icosahedron"].var_array = [[22, 24, f'{rv:02}']]

    return func


def popup_function(context):
    if "Right" in mouse_event(context):
        for index, block in context.modules.items():
            if block.render: block.active = True
        context.mouse_state = (0, 0, 0, 0, 0)
        context.modules["Popup"].render = False
        context.modules["Popup"].active = False
    if "Scroll Up" in mouse_event(context):
        context.modules["Popup"].scroll = max(0, context.modules["Popup"].scroll - 1)
    if "Scroll Down" in mouse_event(context):
        context.modules["Popup"].scroll = min(len(context.modules["Popup"].text.split("\n")) - 3,
                                              context.modules["Popup"].scroll + 1)
    update_popup(context)


def activate_popup(context, text=None):
    for index, block in context.modules.items():
        block.active = False
    context.modules["Popup"].render = True
    context.modules["Popup"].active = True
    context.modules["Popup"].text = text
    context.modules["Popup"].scroll = 0
    update_popup(context)


def update_popup(context):
    text = context.modules["Popup"].text
    scroll_offset = context.modules["Popup"].scroll
    temp_var_array = [[0, 50, f'{scroll_offset}']]
    line_number = 0
    for paragraph in text.split('\n'):
        for chunk in [paragraph[i:i + 49] for i in range(0, len(paragraph), 49)]:
            temp_var_array += [[line_number - scroll_offset + 20, 16, chunk]]
            line_number += 1
    scroll_offset = min(len(temp_var_array), scroll_offset)
    context.modules["Popup"].var_array = temp_var_array[scroll_offset + 1:scroll_offset + 20]


def get_mouse(context):
    old_mouse_state = list(context.mouse_state)
    new_mouse_state = list(curses.getmouse())
    for attribute in range(len(new_mouse_state)):
        if new_mouse_state[attribute] < 0:
            new_mouse_state[attribute] = old_mouse_state[attribute]
    context.mouse_state = tuple(new_mouse_state)

def mouse_event(context):
    code = context.mouse_state[-1]
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
