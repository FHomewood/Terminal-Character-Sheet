from sheet_variables import *

import json
from numpy import floor
from pathlib import Path

Json_path = Path(__file__).parent/"char_state.json"

def change_char_name(context):
	if not context.character: return
	if mouse_event(context) == "Double Left Click":
		if context.character.name == 'Prof. Featherwise':
			context.character.name = 'Prof. Featherwings'
		else:
			context.character.name = 'Prof. Featherwise'

def init(context):
	context.character = Character()
	path = Path(__file__).parent
	context.character.owls = {}
	for owl in [character_module for character_module in path.glob('owls/*.py')]:
		context.character.owls[f'{owl.stem}'] = __import__(f"{owl.parent.parent.parent.stem}.{owl.parent.parent.stem}.{owl.parent.stem}.{owl.stem}", globals(), locals(), ['init','update','exit'],0)



	context.character.name = 'Prof. Featherwise'
	context.character._class =  'Wizard'
	context.character.level = 1
	context.character.prof = 2
	context.character.hit_dice = 'd6'

	context.character.saving_throws = ['INT', 'WIS']
	context.character.skill_proficiencies += ['Arcana', 'Investigation']

	context.character.features = \
	{
		"Proficiencies":{
			"Weapons":{ },
			"Tools":{ },
			"Languages":{ }
		},
		"Features & Traits":{
			"Racial Traits": { },
			"Class Features": { }
		},
		"Inventory":{
			"Equipment":{ },
			"Backpack":{ },
			"Treasures":{ }
		},
		"Spellbook":{ }
	}

	context.character.features["Proficiencies"]["Weapons"]["Daggers"] = """Light weapons capable of being thrown, ideal for use in utility or in combat situations. Getting in close contact with an enemy should be a mage's last resort. However, having something sharp makes it a much more survivable scenario."""
	context.character.features["Proficiencies"]["Weapons"]["Darts"] = """A simple ranged weapon with finesse. With the right skill a well placed dart can finish off a wounded foe or distract a brute. Though you should likely steer clear of attracting too much attention."""
	context.character.features["Proficiencies"]["Weapons"]["Slings"] = """Slings are simple ranged weapons that propel pellet ammunition towards their target. Dangerous at a distance these weapons aren't usually recommended in close quarters."""
	context.character.features["Proficiencies"]["Weapons"]["Quarterstaffs"] = """A mage's familiar staff. Useful in keeping one foot in front of the other as well as packing a punch in combat. Never underestimate the danger these pose by a skilled user."""
	context.character.features["Proficiencies"]["Weapons"]["Light Crossbows"] = """Light crossbows are often weildable in an offhand making them a deadly accompaniment while you cast spells with your free hand. Your foes will rarely expect a bolt coming from your direction."""
	context.character.features["Features & Traits"]["Class Features"]["Arcane Recovery"] = '''You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher.For example, if you’re a 4th-level wizard, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level spell slot or two 1st-level spell slots.'''
	context.character.features["Inventory"]["Equipment"]["Quarterstaff"] = Item(
					name="Quarterstaff",
					description='''A simple melee weapon, grown from an ash tree this staff is a suitable accompaniment to any traveller. A one handed attack with this quarterstaff may deal 1d6 of bludgeoning damage or alternatively a two handed strike can deal 1d8 points of bludgeoning damage''',
					weight=4,
					value=20)
	context.character.features["Inventory"]["Equipment"]["Feathered Robes"] = Item(
					name="Feathered Robes",
					description='''Adventuring gear''',
					weight=4,
					value=100)
	context.character.features["Inventory"]["Equipment"]["Component Pouch"] = Item(
					name="Component Pouch",
					description='''A component pouch is a small, watertight leather belt pouch that has compartments to hold all the material components and other special items you need to cast your spells, except for those components that have a specific cost (as indicated in a spell's description).''',
					weight=2,
					value=2500)
	context.character.features["Inventory"]["Equipment"]["Scholar's Pack"] = Item(
					name="Scholar's Pack",
					description='''Includes a backpack, a book of lore (herbalism), a bottle of ink, an ink pen, 10 sheets of parchment, a little bag of sand, and a small knife.''',
					weight=10,
					value=40000)
	context.character.features["Inventory"]["Equipment"]["Spellbook"] = Item(
					name="Spellbook",
					description='''Essential for wizards, a spellbook is a leather-bound tome with 100 blank vellum pages suitable for recording spells.''',
					weight=3,
					value=5000)
	context.character.features["Inventory"]["Backpack"]["Book of Herbalism"] = Item(
					name="Book of Herbalism",
					description="""A leatherbound journal of horticulture, the growth patterns and notable effects of a number of plants. The book displays common and uncommon foliage found around the Rotten Isles illustrated and described in detail.""",
					weight=5,
					value=2500)
	context.character.features["Inventory"]["Backpack"]["Bottle of ink"] = Item(
					name="Bottle of ink",
					description="""Essential for any scribe, a one ounce glass bottle of black ink. Can be used for drafting notes and calculations, in the wrong hands can also be a forgers best friend.""",
					weight = 0,
					value=1000)
	context.character.features["Inventory"]["Backpack"]["Ink Pen"] = Item(
					name="Ink Pen",
					description="""A quilled pen used by scholars and scribes to take notes""",
					weight = 0,
					value=2)
	context.character.features["Inventory"]["Backpack"]["Sheet of Parchment"] = Item(
					name="Sheet of Parchment",
					description="""A sheet of thick, quality parchment can be bound into a book for """,
					weight = 0,
					value=10,
					quantity = 10)
	context.character.features["Inventory"]["Backpack"]["A Little Bag of Sand"] = Item(
					name="A Little Bag of Sand",
					description="""It's rough and it's coarse and it gets everywhere""",
					weight = 0,
					value=5)
	context.character.features["Inventory"]["Backpack"]["Small Knife"] = Item(
					name="Small Knife",
					description="""A utility knife for when buttering bread with a great-axe feels like overkill""",
					weight = 1,
					value=50)
	context.character.features["Proficiencies"]["Languages"]["Common"] = '''The lingua franca accross all races. The origins of the common tongue is not known, but it enables vast diplomacy across diverse kingdoms.'''



	with open(Json_path) as _file:
		char_state = json.load(_file)

	context.character.owl = char_state['alter']
	context.character.hp = char_state['health']
	context.character.temp_hp = char_state['temp_health']
	context.character.wealth = char_state['coins']

	context.character.owls[context.character.owl].init(context)


def update(context):
	if not context.character: return

	with open(Json_path) as _file:
		char_state = json.load(_file)

	context.character.owl = char_state['alter']
	context.character.hp = char_state['health']
	context.character.temp_hp = char_state['temp_health']
	context.character.wealth = char_state['coins']


	context.art_blocks['Character Name'].var_array = [[10, 21, context.character.name]]
	context.art_blocks['Character Name'].function = change_char_name
	context.art_blocks['Class'].var_array += [[10, 54, context.character._class]]
	context.art_blocks['Level'].var_array += [[10, 63, f'{context.character.level:02}']]
	context.art_blocks['Proficiency Bonus'].var_array += [[17, 13, f'{context.character.prof:+2}']]

	context.art_blocks['STR'].var_array += [[ 16, 4, f'{context.character.str:02}']]
	context.character.str_mod = int(floor((context.character.str-10)/2))
	context.art_blocks['STR'].var_array += [[ 17, 4, f'{context.character.str_mod:+2}']]

	context.art_blocks['DEX'].var_array += [[ 21, 4, f'{context.character.dex:02}']]
	context.character.dex_mod = int(floor((context.character.dex-10)/2))
	context.art_blocks['DEX'].var_array += [[ 22, 4, f'{context.character.dex_mod:+2}']]

	context.art_blocks['CON'].var_array += [[ 26, 4, f'{context.character.con:02}']]
	context.character.con_mod = int(floor((context.character.con-10)/2))
	context.art_blocks['CON'].var_array += [[ 27, 4, f'{context.character.con_mod:+2}']]

	context.art_blocks['INT'].var_array += [[ 31, 4, f'{context.character.int:02}']]
	context.character.int_mod = int(floor((context.character.int-10)/2))
	context.art_blocks['INT'].var_array += [[ 32, 4, f'{context.character.int_mod:+2}']]

	context.art_blocks['WIS'].var_array += [[ 36, 4, f'{context.character.wis:02}']]
	context.character.wis_mod = int(floor((context.character.wis-10)/2))
	context.art_blocks['WIS'].var_array += [[ 37, 4, f'{context.character.wis_mod:+2}']]

	context.art_blocks['CHA'].var_array += [[ 41, 4, f'{context.character.cha:02}']]
	context.character.cha_mod = int(floor((context.character.cha-10)/2))
	context.art_blocks['CHA'].var_array += [[ 42, 4, f'{context.character.cha_mod:+2}']]


	context.art_blocks['Passive Perception'].var_array += [[ 47, 4, f'{10 + ("Perception" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod:02}']]

	context.art_blocks['Acrobatics'].var_array += [
		[ 29, 12, '*' * ('Acrobatics' in context.character.skill_proficiencies)], 
		[ 29, 35, f'{("Acrobatics" in context.character.skill_proficiencies) * context.character.prof + context.character.dex_mod:+2}']]

	context.art_blocks['Animal Handling'].var_array += [
		[ 30, 12, '*' * ('Animal Handling' in context.character.skill_proficiencies)], 
		[ 30, 35, f'{("Animal Handling" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod:+2}']]

	context.art_blocks['Arcana'].var_array += [
		[ 31, 12, '*' * ('Arcana' in context.character.skill_proficiencies)], 
		[ 31, 35, f'{("Arcana" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod:+2}']]

	context.art_blocks['Athletics'].var_array += [
		[ 32, 12, '*' * ('Athletics' in context.character.skill_proficiencies)], 
		[ 32, 35, f'{("Athletics" in context.character.skill_proficiencies) * context.character.prof + context.character.str_mod:+2}']]

	context.art_blocks['Deception'].var_array += [
		[ 33, 12, '*' * ('Deception' in context.character.skill_proficiencies)], 
		[ 33, 35, f'{("Deception" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod:+2}']]

	context.art_blocks['History'].var_array += [
		[ 34, 12, '*' * ('History' in context.character.skill_proficiencies)], 
		[ 34, 35, f'{("History" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod:+2}']]

	context.art_blocks['Insight'].var_array += [
		[ 35, 12, '*' * ('Insight' in context.character.skill_proficiencies)], 
		[ 35, 35, f'{("Insight" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod:+2}']]

	context.art_blocks['Intimidation'].var_array += [
		[ 36, 12, '*' * ('Intimidation' in context.character.skill_proficiencies)], 
		[ 36, 35, f'{("Intimidation" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod:+2}']]

	context.art_blocks['Investigation'].var_array += [
		[ 37, 12, '*' * ('Investigation' in context.character.skill_proficiencies)], 
		[ 37, 35, f'{("Investigation" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod:+2}']]

	context.art_blocks['Medicine'].var_array += [
		[ 38, 12, '*' * ('Medicine' in context.character.skill_proficiencies)], 
		[ 38, 35, f'{("Medicine" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod:+2}']]

	context.art_blocks['Nature'].var_array += [
		[ 39, 12, '*' * ('Nature' in context.character.skill_proficiencies)], 
		[ 39, 35, f'{("Nature" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod:+2}']]

	context.art_blocks['Perception'].var_array += [
		[ 40, 12, '*' * ('Perception' in context.character.skill_proficiencies)], 
		[ 40, 35, f'{("Perception" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod:+2}']]

	context.art_blocks['Performance'].var_array += [
		[ 41, 12, '*' * ('Performance' in context.character.skill_proficiencies)], 
		[ 41, 35, f'{("Performance" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod:+2}']]

	context.art_blocks['Persuasion'].var_array += [
		[ 42, 12, '*' * ('Persuasion' in context.character.skill_proficiencies)], 
		[ 42, 35, f'{("Persuasion" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod:+2}']]

	context.art_blocks['Religion'].var_array += [
		[ 43, 12, '*' * ('Religion' in context.character.skill_proficiencies)], 
		[ 43, 35, f'{("Religion" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod:+2}']]

	context.art_blocks['Sleight of Hand'].var_array += [
		[ 44, 12, '*' * ('Sleight of Hand' in context.character.skill_proficiencies)], 
		[ 44, 35, f'{("Sleight of Hand" in context.character.skill_proficiencies) * context.character.prof + context.character.dex_mod:+2}']]

	context.art_blocks['Stealth'].var_array += [
		[ 45, 12, '*' * ('Stealth' in context.character.skill_proficiencies)], 
		[ 45, 35, f'{("Stealth" in context.character.skill_proficiencies) * context.character.prof + context.character.dex_mod:+2}']]

	context.art_blocks['Survival'].var_array += [
		[ 46, 12, '*' * ('Survival' in context.character.skill_proficiencies)], 
		[ 46, 35, f'{("Survival" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod:+2}']]


	context.art_blocks['STR Saving Throw'].var_array = [[ 22, 18, f'{ ("STR" in context.character.saving_throws) * context.character.prof + context.character.str_mod:+2}']]
	context.art_blocks['DEX Saving Throw'].var_array = [[ 23, 18, f'{ ("DEX" in context.character.saving_throws) * context.character.prof + context.character.dex_mod:+2}']]
	context.art_blocks['CON Saving Throw'].var_array = [[ 24, 18, f'{ ("CON" in context.character.saving_throws) * context.character.prof + context.character.con_mod:+2}']]
	context.art_blocks['INT Saving Throw'].var_array = [[ 22, 30, f'{ ("INT" in context.character.saving_throws) * context.character.prof + context.character.int_mod:+2}']]
	context.art_blocks['WIS Saving Throw'].var_array = [[ 23, 30, f'{ ("WIS" in context.character.saving_throws) * context.character.prof + context.character.wis_mod:+2}']]
	context.art_blocks['CHA Saving Throw'].var_array = [[ 24, 30, f'{ ("CHA" in context.character.saving_throws) * context.character.prof + context.character.cha_mod:+2}']]

	context.character.armour_class = 10+context.character.dex_mod
	context.art_blocks['Armour Class'].var_array += [[ 17, 46, f'{context.character.armour_class:02}']]
	context.art_blocks['Initiative'].var_array += [[ 17, 59, f'{context.character.dex_mod:+2}']]
	context.art_blocks['Speed'].var_array += [[ 17, 73, f'{context.character.spd:02}']]
	context.art_blocks['Hit Points'].var_array += [[ 21, 67, f'{context.character.hp}/{context.character.max_hp}']]
	context.art_blocks["Casting"].var_array += [[ 27, 47, f'{context.character.int_mod:+2}']]
	context.art_blocks['Attack Roll'].var_array += [[ 27, 60, f'{context.character.int_mod + context.character.prof:+2}']]
	context.art_blocks['Spell Save DC'].var_array += [[ 27, 73, f'{8 + context.character.int_mod + context.character.prof}']]

	wealth_str = ''.join([f'{i} ' for i in str(context.character.wealth)])
	context.art_blocks['Coin Pouch'].var_array = [[ 47, 69, f'{wealth_str:>10}']]

	context.art_blocks['Casting'].function = roll(context,1,20,context.character.int_mod)
	context.art_blocks['Attack Roll'].function = roll(context,1,20,context.character.int_mod+context.character.prof)
	context.art_blocks['Initiative'].function = roll(context,1,20,context.character.dex_mod)

	context.art_blocks["STR"].function = roll(context,1,20,context.character.str_mod)
	context.art_blocks["DEX"].function = roll(context,1,20,context.character.dex_mod)
	context.art_blocks["CON"].function = roll(context,1,20,context.character.con_mod)
	context.art_blocks["INT"].function = roll(context,1,20,context.character.int_mod)
	context.art_blocks["WIS"].function = roll(context,1,20,context.character.wis_mod)
	context.art_blocks["CHA"].function = roll(context,1,20,context.character.cha_mod)

	context.art_blocks["Acrobatics"].function = roll(context,1,20,("Acrobatics" in context.character.skill_proficiencies) * context.character.prof + context.character.dex_mod)
	context.art_blocks["Animal Handling"].function = roll(context,1,20,("Animal Handling" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod)
	context.art_blocks["Arcana"].function = roll(context,1,20,("Arcana" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod)
	context.art_blocks["Athletics"].function = roll(context,1,20,("Athletics" in context.character.skill_proficiencies) * context.character.prof + context.character.str_mod)
	context.art_blocks["Deception"].function = roll(context,1,20,("Deception" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod)
	context.art_blocks["History"].function = roll(context,1,20,("History" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod)
	context.art_blocks["Insight"].function = roll(context,1,20,("Insight" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod)
	context.art_blocks["Intimidation"].function = roll(context,1,20,("Intimidation" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod)
	context.art_blocks["Investigation"].function = roll(context,1,20,("Investigation" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod)
	context.art_blocks["Medicine"].function = roll(context,1,20,("Medicine" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod)
	context.art_blocks["Nature"].function = roll(context,1,20,("Nature" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod)
	context.art_blocks["Perception"].function = roll(context,1,20,("Perception" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod)
	context.art_blocks["Performance"].function = roll(context,1,20,("Performance" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod)
	context.art_blocks["Persuasion"].function = roll(context,1,20,("Persuasion" in context.character.skill_proficiencies) * context.character.prof + context.character.cha_mod)
	context.art_blocks["Religion"].function = roll(context,1,20,("Religion" in context.character.skill_proficiencies) * context.character.prof + context.character.int_mod)
	context.art_blocks["Sleight of Hand"].function = roll(context,1,20,("Sleight of Hand" in context.character.skill_proficiencies) * context.character.prof + context.character.dex_mod)
	context.art_blocks["Stealth"].function = roll(context,1,20,("Stealth" in context.character.skill_proficiencies) * context.character.prof + context.character.dex_mod)
	context.art_blocks["Survival"].function = roll(context,1,20,("Survival" in context.character.skill_proficiencies) * context.character.prof + context.character.wis_mod)


	context.art_blocks["STR Saving Throw"].function = roll(context,1,20,("STR" in context.character.saving_throws) * context.character.prof + context.character.str_mod)
	context.art_blocks["DEX Saving Throw"].function = roll(context,1,20,("DEX" in context.character.saving_throws) * context.character.prof + context.character.dex_mod)
	context.art_blocks["CON Saving Throw"].function = roll(context,1,20,("CON" in context.character.saving_throws) * context.character.prof + context.character.con_mod)
	context.art_blocks["INT Saving Throw"].function = roll(context,1,20,("INT" in context.character.saving_throws) * context.character.prof + context.character.int_mod)
	context.art_blocks["WIS Saving Throw"].function = roll(context,1,20,("WIS" in context.character.saving_throws) * context.character.prof + context.character.wis_mod)
	context.art_blocks["CHA Saving Throw"].function = roll(context,1,20,("CHA" in context.character.saving_throws) * context.character.prof + context.character.cha_mod)
	context.art_blocks["Icosahedron"].function = roll(context,1,20,0)

	for i in range(16):
		current_feature = context.character.features
		for key in context.feature_box_keys:
			current_feature = current_feature[key]
		headings = list(current_feature.keys())
		if context.feature_box_keys == []:
			title_text = "~ Features ~"
		else: 
			title_text = f'~ {context.feature_box_keys[-1]} ~'
		context.art_blocks["Features Box"].var_array = [[31,61-len(title_text)//2,title_text]]
		scroll_offset = context.art_blocks["Features Box"].scroll

		if len(headings) > i + scroll_offset:
			context.art_blocks[f'Features Line {i}'].var_array = [[32+i,44,f'{headings[i+scroll_offset]}']]
		else:
			context.art_blocks[f'Features Line {i}'].var_array = [[0,0,'']]

		context.character.owls[context.character.owl].update(context)
