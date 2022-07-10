from sheet_variables import *
def init(context):
	context.character.int += 17
	context.character.str += 11
	context.character.wis += 12
	context.character.con += 15
	context.character.dex += 16
	context.character.cha += 12

	context.character.race = 'Gnome'
	context.character.int += 2
	context.character.spd = 25

	context.character.features["Features & Traits"]["Racial Traits"]["Darkvision"] = '''Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.'''
	context.character.features["Features & Traits"]["Racial Traits"]["Gnome Cunning"] = '''You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.'''
	context.character.features["Proficiencies"]["Languages"]["Common"] = None
	context.character.features["Proficiencies"]["Languages"]["Gnomish"] = None

	context.character.subrace = "Forest Gnome"
	context.character.dex += 1
	context.character.features["Spellbook"]["Minor Illusion"] = Spell(
		name="Minor Illusion",
		description='''You create a sound or an image of an object within range that lasts for the duration. The illusion also ends if you dismiss it as an action or cast this spell again. If you create a sound, its volume can range from a whisper to a scream. It can be your voice, someone else’s voice, a lion’s roar, a beating of drums, or any other sound you choose. The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends. If you create an image of an object—such as a chair, muddy footprints, or a small chest—it must be no larger than a 5-foot cube. The image can’t create sound, light, smell, or any other sensory effect. Physical interaction with the image reveals it to be an illusion, because things can pass through it. If a creature uses its action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.''',
		school="Illusion",
		level=0,
		cast_time="1 action",
		range="30ft",
		somatic=True,
		material="a bit of fleece",
		duration="1 minute")
	context.character.features["Features & Traits"]["Racial Traits"]['Speak with Small Beasts'] = '''Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.'''

	context.character.max_hp += 6 + 2

	context.character.background = "Travelling Psychic"
	context.character.skill_proficiencies += ["Persuasion", "Performance"]
	context.character.features["Proficiencies"]["Languages"]["Dwarvish"] = None
	context.character.features["Proficiencies"]["Tools"]["Dice Set"] = None


	context.character.features["Spellbook"]["Prestidigitation"] = Spell(
		name="Prestidigitation",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Mind Sliver"] = Spell(
		name="Mind Sliver",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Gust"] = Spell(
		name="Gust",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Mage Armour"] = Spell(
		name="Mage Armour",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Feather Fall"] = Spell(
		name="Feather Fall",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Hideous Laughter"] = Spell(
		name="Hideous Laughter",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Silvery Barbs"] = Spell(
		name="Silvery Barbs",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Detect Magic"] = Spell(
		name="Detect Magic",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Magic Missile"] = Spell(
		name="Magic Missile",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)


	context.character.level = 2
	context.character.max_hp += 4 + 2
	context.character.features["Features & Traits"]["Class Features"]['Portent'] = """Starting at 2nd level when you choose this school, glimpses of the future begin to press in on your awareness. When you finish a long rest, roll two d20s and record the numbers rolled. You can replace any attack roll, saving throw, or ability check made by you or a creature that you can see with one of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only once per turn. Each foretelling roll can be used only once. When you finish a long rest, you lose any unused foretelling rolls."""

	context.character.features["Spellbook"]["Comprehend Languages"] = Spell(
		name="Comprehend Languages",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.features["Spellbook"]["Distort Value"] = Spell(
		name="Distort Value",
		description=None,
		school=None,
		level=None,
		cast_time=None,
		range=None,
		concentration=None,
		ritual=None,
		verbal=None,
		somatic=None,
		material=None,
		duration=None,
		function=None)

	context.character.max_hp += 6 + 2

def update(context):
	pass