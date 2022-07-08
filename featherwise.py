import eenie
import laucian
import runin

import json
from sheet_variables import *

class Character:
	def __init__(self):
		self.name = ""
		self.alignment = ""
		self._class = ""

		self.int = 0
		self.str = 0
		self.wis = 0
		self.con = 0
		self.dex = 0
		self.cha = 0

		self.xp = 0
		self.money = 0

		self.features = {}
		self.skill_proficiencies = []

class Item:
	def __init__(self, name=None,description=None,weight=None,value=None, quantity=1):
		self.name = name
		self.description = description
		self.weight = weight
		self.value = value
		self.quantity = quantity

class Spell:
	def __init__(self,
		name=None,description=None,school=None,level=None,cast_time=None,
		range=None,concentration=None,ritual=None,verbal=None,somatic=None,
		material=None,duration=None,function=None):
			self.name = name
			self.description = description
			self.school = school
			self.level = level
			self.cast_time = cast_time
			self.range = range
			self.concentration = concentration
			self.ritual = ritual
			self.verbal = verbal
			self.somatic =somatic
			self.material = material
			self.duration = duration
			self.function = function

def change_char_name(context):
	if not context.character: return
	if mouse_event(context) == "Double Left Click":
		if context.character.name == 'Prof. Featherwise':
			context.character.name = 'Prof. Featherwings'
		else:
			context.character.name = 'Prof. Featherwise'

def init(context):
	context.character = Character()

	with open('./char_state.json') as _file:
		char_state = json.load(_file)

	{	'eenie': eenie,
		'laucian': laucian,
		'runin': runin,		} [ char_state['alter'] ].init(context)

	context.character.name = 'Prof. Featherwise'
	context.character.alter = char_state['alter']
	context.character._class =  'Wizard'
	context.character.hit_dice = 'd8'

	context.character.saving_throws = ['INT', 'WIS']
	context.character.skill_proficiencies += ['Arcana', 'Investigation']

	context.character.features = \
	{
		"Proficiencies":{
			"Skills":{

			},
			"Weapons":{
				"Dagger": None,
				"Dart": None,
				"Sling": None,
				"Quarterstaff": None,
				"Light Crossbow": None
			},
			"Tools":{

			},
			"Languages":{

			}
		},
		"Features & Traits":{
			"Racial Traits": {

			},
			"Class Features": {
				"Arcane Recovery": '''You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher.For example, if you’re a 4th-level wizard, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level spell slot or two 1st-level spell slots.''',

			}
		},
		"Spellbook":{

		},
		"Inventory":{
			"Equipment":{
				"Quarterstaff": Item(
					name="Quarterstaff",
					description='''A simple melee weapon, grown from an ash tree this staff is a suitable accompaniment to any traveller. A one handed attack with this quarterstaff may deal 1d6 of bludgeoning damage or alternatively a two handed strike can deal 1d8 points of bludgeoning damage''',
					weight="4 lbs",
					value=20),
				"Feathered Robes": Item(
					name="Feathered Robes",
					description='''Adventuring gear''',
					weight="4 lbs",
					value=100),
				"Component Pouch": Item(
					name="Component Pouch",
					description='''A component pouch is a small, watertight leather belt pouch that has compartments to hold all the material components and other special items you need to cast your spells, except for those components that have a specific cost (as indicated in a spell's description).''',
					weight="2 lbs",
					value=2500),
				"Scholar's Pack": Item(
					name="Scholar's Pack",
					description='''Includes a backpack, a book of lore (herbalism), a bottle of ink, an ink pen, 10 sheets of parchment, a little bag of sand, and a small knife.''',
					weight="10 lbs",
					value=40000),
				"Spellbook": Item(
					name="Spellbook",
					description='''Essential for wizards, a spellbook is a leather-bound tome with 100 blank vellum pages suitable for recording spells.''',
					weight="3 lbs",
					value=5000)
			},
			"Backpack":{
				"Book of Herbalism": Item(
					name="Book of Herbalism",
					description=""" """,
					weight="5 lbs",
					value=2500),
				"Bottle of ink": Item(
					name="Bottle of ink",
					description=""" """,
					weight="",
					value=0),
				"Ink Pen": Item(
					name="Ink Pen",
					description=""" """,
					weight="",
					value=0),
				"Sheet of Parchment": Item(
					name="Sheet of Parchment",
					description=""" """,
					weight="",
					value=0,
					quantity = 10),
				"A Little Bag of Sand": Item(
					name="A Little Bag of Sand",
					description=""" """,
					weight="",
					value=0),
				"Small Knife": Item(
					name="Small Knife",
					description=""" """,
					weight="",
					value=0),
			},
			"Treasures":{

			}
		}
	}
	context.feature_box_keys = []

	# context.character.equipment['Spellbook'] = {
	# 		'Description': ''
	# 	}
	# context.character.inventory += ['Book of Lore', 'Bottle of Ink', 'Ink Pen', '10 Sheets of Parchment', 'Little Bag of Sand', 'Small Knife']
	# context.character.features_and_traits['Ritual Casting'] = '''You can cast a wizard spell as a ritual if that spell has the ritual tag and you have the spell in your spellbook. You don't need to have the spell prepared.'''

		# First session
	# context.character.xp += 225

		# Second session
		
		# Third session


def update(context):
	if not context.character: return
	context.art_blocks['Character Name'].var_array = [[10, 21, context.character.name]]
	context.art_blocks['Character Name'].function = change_char_name
	context.art_blocks['Class'].var_array += [[10, 54, 'Wizard']]
	context.art_blocks['Level'].var_array += [[10, 63, '02']]
	context.art_blocks['Proficiency Bonus'].var_array += [[17, 13, '+2']]

	for i in range(16):
		headings = list(context.get_current_feature().keys())

		if len(headings) > i:
			context.art_blocks[f'Features Line {i}'].var_array = [[32+i,44,f'{headings[i]}']]
		else:
			context.art_blocks[f'Features Line {i}'].var_array = [[0,0,'']]
