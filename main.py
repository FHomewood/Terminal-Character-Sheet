import curses
from pathlib import Path

from sheet_variables import *

class Context:
	def __init__(self):
		self.stdscr = None
		self.screen_state = "character_select"
		self.art_blocks = {}
		self.mouse_state = (0,0,0,0,0)
		self.character = None
		self.feature_box_keys = []

	def get_current_feature(self):
		current_dict = self.character.features
		for i in self.feature_box_keys:
			current_dict = current_dict[i]
		return current_dict


def init(context):

	context.stdscr = curses.initscr()
	curses.start_color()
	curses.noecho()
	curses.cbreak()
	context.stdscr.keypad(1)
	context.stdscr.leaveok(1)
	curses.resize_term(52, 82)
	curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

	curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
	curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
	curses.init_pair(4,curses.COLOR_CYAN,curses.COLOR_BLACK)
	curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
	curses.init_pair(6,curses.COLOR_YELLOW,curses.COLOR_BLACK)

	define_art_blocks(context)

	path = Path(__file__).parent
	character_paths = [character_module for character_module in path.glob('characters/*/*.py')]

	activate_popup(context,"")
	for index, character in enumerate(character_paths):
		context.art_blocks[f"select_{character.parent.name}"] = InteractiveBlock( (23 + 2 * index, 21), 4, f"{character.parent.name}")
		context.art_blocks[f"select_{character.parent.name}"].function = import_char(context,character)

def import_char(context,char_path):
	def func(context):
		if mouse_event(context) =="Double Left Click":
			context.character_module = __import__(f"characters.{char_path.parent.name}.{char_path.stem}", globals(), locals(), ["init", "update","end"], 0)
			for key, block in context.art_blocks.items():
				if key.startswith("select_"):
					block.render = False
					block.active = False
				if block.render: block.active = True
			context.mouse_state = (0,0,0,0,0)
			context.art_blocks["Popup"].render = False
			context.art_blocks["Popup"].active = False

			context.character_module.init(context)
	return func


def update(context):
	context.stdscr.clear()
	get_mouse(context)

	for identifier, block in context.art_blocks.items():
		if block.mouse_in_block(context) and \
		   block.active and \
		   block.function:
			block.function(context)


def draw(context):
	for identifier, block in context.art_blocks.items():
		block.draw(context)
	context.stdscr.addstr(0,0,str(f"y:{context.mouse_state[2]}, x:{context.mouse_state[1]} || {mouse_event(context)}"))


def end(context):
	curses.nocbreak()
	context.stdscr.keypad(False)
	curses.echo()
	curses.endwin()

if __name__ == "__main__":
	context = Context()
	init(context)
	while True:
		update(context)
		if context.character: context.character_module.update(context)
		draw(context)
		context.stdscr.refresh()

		key = context.stdscr.getch()
		if key == ord('q'):
			break

	end(context)
