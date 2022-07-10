import eenie
import laucian
import runin

import json
from sheet_variables import *


def change_char_name(context):
	if not context.character: return
	if mouse_event(context) == "Double Left Click":
		if context.character.name == 'Prof. Featherwise':
			context.character.name = 'Prof. Featherwings'
		else:
			context.character.name = 'Prof. Featherwise'

def init(context):
	context.character = Character()


	context.character.name = 'Prof. Featherwise'
	context.character._class =  'Wizard'
	context.character.level = 1
	context.character.prof = 2
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

	with open('./char_state.json') as _file:
		context.character.owl = json.load(_file)['alter']

	{	'eenie': eenie,
		'laucian': laucian,
		'runin': runin,		} [ context.character.owl ].init(context)


def update(context):
	if not context.character: return
	context.art_blocks['Character Name'].var_array = [[10, 21, context.character.name]]
	context.art_blocks['Character Name'].function = change_char_name
	context.art_blocks['Class'].var_array += [[10, 54, context.character._class]]
	context.art_blocks['Level'].var_array += [[10, 63, f'{context.character.level}']]
	context.art_blocks['Proficiency Bonus'].var_array += [[17, 13, f'{context.character.prof}']]

	context.art_blocks['STR'].var_array += [[ 16, 4, '08']]
	context.art_blocks['STR'].var_array += [[ 17, 4, '-1']]

	context.art_blocks['DEX'].var_array += [[ 21, 4, '14']]
	context.art_blocks['DEX'].var_array += [[ 22, 4, '+2']]

	context.art_blocks['CON'].var_array += [[ 26, 4, '14']]
	context.art_blocks['CON'].var_array += [[ 27, 4, '+2']]

	context.art_blocks['INT'].var_array += [[ 31, 4, '18']]
	context.art_blocks['INT'].var_array += [[ 32, 4, '+4']]

	context.art_blocks['WIS'].var_array += [[ 36, 4, '13']]
	context.art_blocks['WIS'].var_array += [[ 37, 4, '+1']]

	context.art_blocks['CHA'].var_array += [[ 41, 4, '12']]
	context.art_blocks['CHA'].var_array += [[ 42, 4, '+1']]

	context.art_blocks['Passive Perception'].var_array += [[ 47, 4, '11']]

	context.art_blocks['Acrobatics'].var_array += [
		[ 29, 12, '*' * ('Acrobatics' in context.character.skill_proficiencies)], 
		[ 29, 35, '+2']]
	context.art_blocks['Animal Handling'].var_array += [
		[ 30, 12, '*' * ('Animal Handling' in context.character.skill_proficiencies)], 
		[ 30, 35, '+1']]
	context.art_blocks['Arcana'].var_array += [
		[ 31, 12, '*' * ('Arcana' in context.character.skill_proficiencies)], 
		[ 31, 35, '+6']]
	context.art_blocks['Athletics'].var_array += [
		[ 32, 12, '*' * ('Athletics' in context.character.skill_proficiencies)], 
		[ 32, 35, '-1']]
	context.art_blocks['Deception'].var_array += [
		[ 33, 12, '*' * ('Deception' in context.character.skill_proficiencies)], 
		[ 33, 35, '+1']]
	context.art_blocks['History'].var_array += [
		[ 34, 12, '*' * ('History' in context.character.skill_proficiencies)], 
		[ 34, 35, '+4']]
	context.art_blocks['Insight'].var_array += [
		[ 35, 12, '*' * ('Insight' in context.character.skill_proficiencies)], 
		[ 35, 35, '+1']]
	context.art_blocks['Intimidation'].var_array += [
		[ 36, 12, '*' * ('Intimidation' in context.character.skill_proficiencies)], 
		[ 36, 35, '+1']]
	context.art_blocks['Investigation'].var_array += [
		[ 37, 12, '*' * ('Investigation' in context.character.skill_proficiencies)], 
		[ 37, 35, '+6']]
	context.art_blocks['Medicine'].var_array += [
		[ 38, 12, '*' * ('Medicine' in context.character.skill_proficiencies)], 
		[ 38, 35, '+1']]
	context.art_blocks['Nature'].var_array += [
		[ 39, 12, '*' * ('Nature' in context.character.skill_proficiencies)], 
		[ 39, 35, '+4']]
	context.art_blocks['Perception'].var_array += [
		[ 40, 12, '*' * ('Perception' in context.character.skill_proficiencies)], 
		[ 40, 35, '+1']]
	context.art_blocks['Performance'].var_array += [
		[ 41, 12, '*' * ('Performance' in context.character.skill_proficiencies)], 
		[ 41, 35, '+1']]
	context.art_blocks['Persuasion'].var_array += [
		[ 42, 12, '*' * ('Persuasion' in context.character.skill_proficiencies)], 
		[ 42, 35, '+1']]
	context.art_blocks['Religion'].var_array += [
		[ 43, 12, '*' * ('Religion' in context.character.skill_proficiencies)], 
		[ 43, 35, '+4']]
	context.art_blocks['Sleight of Hand'].var_array += [
		[ 44, 12, '*' * ('Sleight of Hand' in context.character.skill_proficiencies)], 
		[ 44, 35, '+2']]
	context.art_blocks['Stealth'].var_array += [
		[ 45, 12, '*' * ('Stealth' in context.character.skill_proficiencies)], 
		[ 45, 35, '+2']]
	context.art_blocks['Survival'].var_array += [
		[ 46, 12, '*' * ('Survival' in context.character.skill_proficiencies)], 
		[ 46, 35, '+1']]

	context.art_blocks['Saving Throws'].var_array += [[ 22, 18, '-1']]
	context.art_blocks['Saving Throws'].var_array += [[ 23, 18, '+2']]
	context.art_blocks['Saving Throws'].var_array += [[ 24, 18, '+2']]
	context.art_blocks['Saving Throws'].var_array += [[ 22, 30, '+6']]
	context.art_blocks['Saving Throws'].var_array += [[ 23, 30, '+3']]
	context.art_blocks['Saving Throws'].var_array += [[ 24, 30, '+1']]

	context.art_blocks['Armour Class'].var_array += [[ 17, 46, '12']]
	context.art_blocks['Initiative'].var_array += [[ 17, 59, '+2']]
	context.art_blocks['Speed'].var_array += [[ 17, 73, '30']]
	context.art_blocks['Hit Points'].var_array += [[ 21, 67, '16']]
	context.art_blocks["Casting"].var_array += [[ 27, 47, '+4']]
	context.art_blocks['Attack Roll'].var_array += [[ 27, 60, '+6']]
	context.art_blocks['Spell Save DC'].var_array += [[ 27, 73, '14']]


	for i in range(16):
		headings = list(context.get_current_feature().keys())

		if len(headings) > i:
			context.art_blocks[f'Features Line {i}'].var_array = [[32+i,44,f'{headings[i]}']]
		else:
			context.art_blocks[f'Features Line {i}'].var_array = [[0,0,'']]

	{	'eenie': eenie,
		'laucian': laucian,
		'runin': runin,		} [ context.character.owl ].update(context)
