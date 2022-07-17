from sheet_variables import *

from numpy import floor
from pathlib import Path


def init(context):
	context.character = Character()

	context.character.name = 'Corrin TossCobble'
	context.character._class =  'Bard'
	context.character.hit_dice = 'd8'
	context.character.level = 8
	context.character.prof = 3
	context.character.max_hp = 72
	context.character.hp = 72
	context.character.spd = 25

	context.character.saving_throws = ['DEX', 'CHA']
	context.character.skill_proficiencies += ['Arcana', 'Deception', 'History', 'Insight', 'Intimidation', 'Perception', 'Performance', 'Persuasion']
	context.character.skill_expertise = ['Deception', 'Persuasion']
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
	context.character.features["Proficiencies"]["Languages"]["Common"] = '''The lingua franca accross all races. The origins of the common tongue is not known, but it enables vast diplomacy across diverse kingdoms.'''
	context.character.int = 13
	context.character.str = 9
	context.character.wis = 14
	context.character.con = 16
	context.character.dex = 18
	context.character.cha = 20

	context.character.xp = 0
	context.character.wealth = 0
	context.character.features["Features & Traits"]["Class Features"]["Jack of all Trades"] = """You can add half your proficiency bonus, rounded down ( +1 ), to any ability check you make that doesn’t already include it."""
	context.character.features["Features & Traits"]["Class Features"]["Song of Rest"] = """If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points."""
	context.character.features["Features & Traits"]["Class Features"]["Bardic Inspiration"] = """As a bonus action, a creature (other than you) within 60 ft. that can hear you gains an inspiration die (1d8). For 10 minutes, the creature can add it to one ability check, attack roll, or saving throw. This can be added after seeing the roll, but before knowing the outcome."""
	context.character.features["Features & Traits"]["Class Features"]["Cutting Words"] = """As a reaction when a creature (that's not immune to being charmed) you can see within 60 ft. makes an attack roll, ability check, or damage roll, you can expend one use of Bardic Inspiration, roll the die, and subtract the number from the creature's roll. You can do so after the roll but before knowing the result."""
	context.character.features["Features & Traits"]["Class Features"]["Counter Charm"] = """As an action, you can perform until the end of your next turn. During that time, you and any friendly creatures within 30 ft. that can hear you gain advantage on saving throws against being frightened or charmed."""


def update(context):
	if not context.character: return

	context.art_blocks['Character Name'].var_array = [[10, 21, context.character.name]]
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
		headings = list(context.get_current_feature().keys())
		if context.feature_box_keys == []:
			title_text = "~ Features ~"
		else: 
			title_text = f'~ {context.feature_box_keys[-1]} ~'
		context.art_blocks["Features Box"].var_array = [[31,61-len(title_text)//2,title_text]]
		scroll_offset = context.art_blocks["Features Box"].scroll

		if len(headings) > i+scroll_offset:
			context.art_blocks[f'Features Line {i}'].var_array = [[32+i,44,f'{headings[i+scroll_offset]}']]
		else:
			context.art_blocks[f'Features Line {i}'].var_array = [[0,0,'']]
