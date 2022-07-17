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
	context.character.features["Proficiencies"]["Languages"]["Gnomish"] = """The Gnomish language, which uses the Dwarvish script, is renowned for its technical treatises and its catalogs of knowledge about the natural world."""

	context.character.subrace = "Forest Gnome"
	context.character.dex += 1
	context.character.features["Spellbook"]["Minor Illusion"] = Spell(
		name="Minor Illusion",
		description='''You create a sound or an image of an object within range that lasts for the duration. The illusion also ends if you dismiss it as an action or cast this spell again.

If you create a sound, its volume can range from a whisper to a scream. It can be your voice, someone else's voice, a lion's roar, a beating of drums, or any other sound you choose. The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends.

If you create an image of an object—such as a chair, muddy footprints, or a small chest—it must be no larger than a 5-foot cube. The image can't create sound, light, smell, or any other sensory effect. Physical interaction with the image reveals it to be an illusion, because things can pass through it.

If a creature uses its action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.''',
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
	context.character.features["Proficiencies"]["Languages"]["Dwarvish"] = "Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak."
	context.character.features["Proficiencies"]["Tools"]["Dice Set"] = "If you are proficient with a gaming set, you can add your proficiency bonus to ability checks you make to play a game with that set. Each type of gaming set requires a separate proficiency."


	context.character.features["Spellbook"]["Prestidigitation"] = Spell(
		name="Prestidigitation",
		description="""This spell is a minor magical trick that novice spellcasters use for practice. You create one of the following magical effects within range:

* You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor.

* You instantaneously light or snuff out a candle, a torch, or a small campfire.

* You instantaneously clean or soil an object no larger than 1 cubic foot.

* You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour.

* You make a color, a small mark, or a symbol appear on an object or a surface for 1 hour.

* You create a nonmagical trinket or an illusory image that can fit in your hand and that lasts until the end of your next turn.

If you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action.""",
		school="Transmutation ",
		level=0,
		cast_time="1 action",
		range="10 ft",
		verbal=True,
		somatic=True,
		duration="Up to 1 hour")

	context.character.features["Spellbook"]["Mind Sliver"] = Spell(
		name="Mind Sliver",
		description='''You drive a disorienting spike of psychic energy into the mind of one creature you can see within range. The target must succeed on an Intelligence saving throw or take 1d6 psychic damage and subtract 1d4 from the next saving throw it makes before the end of your next turn.

This spell's damage increases by 1d6 when you reach certain levels: 5th level (2d6), 11th level (3d6), and 17th level (4d6).''',
		school="Enchantment ",
		level=0,
		cast_time="1 action",
		range="60 ft",
		verbal=True,
		duration="1 round")

	context.character.features["Spellbook"]["Gust"] = Spell(
		name="Gust",
		description='''You seize the air and compel it to create one of the following effects at a point you can see within range:

* One Medium or smaller creature that you choose must succeed on a Strength saving throw or be pushed up to 5 feet away from you.

* You create a small blast of air capable of moving one object that is neither held nor carried and that weighs no more than 5 pounds. The object is pushed up to 10 feet away from you. It isn't pushed with enough force to cause damage.

* You create a harmless sensory effect using air, such as causing leaves to rustle, wind to slam shutters closed, or your clothing to ripple in a breeze.''',
		school="Transmutation ",
		level=0,
		cast_time="1 action",
		range="30 ft",
		verbal=True,
		somatic=True,
		duration="Instantaneous")

	context.character.features["Spellbook"]["Mage Armour"] = Spell(
		name="Mage Armour",
		description='''You touch a willing creature who isn't wearing armor, and a protective magical force surrounds it until the spell ends. The target's base AC becomes 13 + its Dexterity modifier. The spell ends if the target dons armor or if you dismiss the spell as an action.''',
		school="Abjuration",
		level=1,
		cast_time="1 action",
		range="Touch",
		verbal=True,
		somatic=True,
		material="a piece of cured leather",
		duration="8 hours")

	context.character.features["Spellbook"]["Feather Fall"] = Spell(
		name="Feather Fall",
		description='''Choose up to five falling creatures within range. A falling creature's rate of descent slows to 60 feet per round until the spell ends. If the creature lands before the spell ends, it takes no falling damage and can land on its feet, and the spell ends for that creature.''',
		school="transmutation",
		level=1,
		cast_time="1 reaction",
		range="60 ft",
		verbal=True,
		material="a small feather",
		duration="1 minute")

	context.character.features["Spellbook"]["Hideous Laughter"] = Spell(
		name="Hideous Laughter",
		description='''A creature of your choice that you can see within range perceives everything as hilariously funny and falls into fits of laughter if this spell affects it. The target must succeed on a Wisdom saving throw or fall prone, becoming incapacitated and unable to stand up for the duration. A creature with an Intelligence score of 4 or less isn't affected.

At the end of each of its turns, and each time it takes damage, the target can make another Wisdom saving throw. The target has advantage on the saving throw if it's triggered by damage. On a success, the spell ends.''',
		school="enchantment",
		level=1,
		cast_time="1 action",
		range="30 ft",
		concentration=True,
		verbal=True,
		somatic=True,
		material="tiny tarts and a feather",
		duration="Up to 1 minute")

	context.character.features["Spellbook"]["Silvery Barbs"] = Spell(
		name="Silvery Barbs",
		description='''You magically distract the triggering creature and turn its momentary uncertainty into encouragement for another creature. The triggering creature must reroll the d20 and use the lower roll.

You can then choose a different creature you can see within range (you can choose yourself). The chosen creature has advantage on the next attack roll, ability check, or saving throw it makes within 1 minute. A creature can be empowered by only one use of this spell at a time.''',
		school="enchantment",
		level=1,
		cast_time="1 reaction",
		range="60 ft",
		verbal=True,
		duration="Instantaneous")

	context.character.features["Spellbook"]["Detect Magic"] = Spell(
		name="Detect Magic",
		description='''For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.

The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.''',
		school="divination",
		level=1,
		cast_time="1 action",
		range="Self",
		concentration=True,
		ritual=True,
		verbal=True,
		somatic=True,
		duration="Up to 10 minutes")

	context.character.features["Spellbook"]['Magic Missile'] = Spell(
		name='Magic Missile',
		description= '''You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously and you can direct them to hit one creature or several.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot level above 1st.''',
		school= 'Evocation' ,
		level= 1 ,
		cast_time= '1 action' ,
		range= '120ft' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Instantaneous')


	context.character.level = 2
	context.character.max_hp += 4 + 2
	context.character.features["Features & Traits"]["Class Features"]['Portent'] = """Starting at 2nd level when you choose this school, glimpses of the future begin to press in on your awareness. When you finish a long rest, roll two d20s and record the numbers rolled. You can replace any attack roll, saving throw, or ability check made by you or a creature that you can see with one of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only once per turn.

Each foretelling roll can be used only once. When you finish a long rest, you lose any unused foretelling rolls."""

	context.character.features["Spellbook"]['Comprehend Languages'] = Spell(
		name='Comprehend Languages',
		description= '''For the duration, you understand the literal meaning of any spoken language that you hear. You also understand any written language that you see, but you must be touching the surface on which the words are written. It takes about 1 minute to read one page of text.

This spell doesn't decode secret messages in a text or a glyph, such as an arcane sigil, that isn't part of a written language.''',
		school= 'Divination' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= 'Self' ,
		verbal= True ,
		somatic= True ,
		material= 'A pinch of soot and salt' ,
		duration= '1 Hour')

	context.character.features["Spellbook"]['Distort Value'] = Spell(
		name='Distort Value',
		description= '''Do you need to squeeze a few more gold pieces out of a merchant as you try to sell that weird octopus statue you liberated from the chaos temple? Do you need to downplay the worth of some magical assets when the tax collector stops by? Distort value has you covered.

You cast this spell on an object no more than 1 foot on a side, doubling the object's perceived value by adding illusory flourishes or polish to it, or reducing its perceived value by half with the help of illusory scratches, dents, and other unsightly features. Anyone examining the object can ascertain its true value with a successful Intelligence (Investigation) check against your spell save DC.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the maximum size of the object increases by 1 foot for each slot level above 1st.''',
		school= 'Illusion' ,
		level= 1 ,
		cast_time= '1 Minute' ,
		range= 'Touch' ,
		verbal= True ,
		somatic= False ,
		material= False ,
		duration= '8 Hours')

	context.character.level = 3
	context.character.max_hp += 6 + 2

	context.character.features["Spellbook"]["Augury"] = Spell(
		name="Augury",
		description='''By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, or employing some other divining tool, you receive an omen from an otherworldly entity about the results of a specific course of action that you plan to take within the next 30 minutes. The DM chooses from the following possible omens:

* Weal, for good results
* Woe, for bad results
* Weal and woe, for both good and bad results
* Nothing, for results that aren't especially good or bad

The spell doesn't take into account any possible circumstances that might change the outcome, such as the casting of additional spells or the loss or gain of a companion.

If you cast the spell two or more times before completing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get a random reading. The DM makes this roll in secret.''',
		school="Divination",
		level=2,
		cast_time="1 minute",
		range="Self",
		ritual=True,
		verbal=True,
		somatic=True,
		material="25 gp of divining trinkets",
		duration="Instantaneous")

	context.character.features["Spellbook"]["Jim's Glowing Coin"] = Spell(
		name="Jim's Glowing Coin",
		description='''Of the many tactics employed by master magician and renowned adventurer Jim Darkmagic, the old glowing coin trick is a time-honored classic. When you cast the spell, you hurl the coin that is the spell's material component to any spot within range. The coin lights up as if under the effect of a light spell. Each creature of your choice that you can see within 30 feet of the coin must succeed on a Wisdom saving throw or be distracted for the duration. While distracted, a creature has disadvantage on Wisdom (Perception) checks and initiative rolls.''',
		school="Enchantment",
		level=2,
		cast_time="1 action",
		range="60 ft",
		ritual=True,
		somatic=True,
		material="a coin",
		duration="1 minute")

	context.character.level = 4
	context.character.max_hp += 5 + 2

	context.character.features["Spellbook"]["Mage Hand"] = Spell(
		name="Mage Hand",
		description='''A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration or until you dismiss it as an action. The hand vanishes if it is ever more than 30 feet away from you or if you cast this spell again.

You can use your action to control the hand. You can use the hand to manipulate an object, open an unlocked door or container, stow or retrieve an item from an open container, or pour the contents out of a vial. You can move the hand up to 30 feet each time you use it.

The hand can't attack, activate magic items, or carry more than 10 pounds.''',
		school="Conjuration",
		level=0,
		cast_time="1 action",
		range="30 ft",
		verbal=True,
		somatic=True,
		duration="1 minute")

	context.character.features["Spellbook"]["Alarm"] = Spell(
		name="Alarm",
		description='''You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible.

A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.

An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.''',
		school="Abjuration",
		level=1,
		cast_time="1 minute",
		range="30 ft",
		ritual=True,
		verbal=True,
		somatic=True,
		material="a tiny bell and a piece of fine silver wire",
		duration="8 hours")

	context.character.features["Spellbook"]["Catapult"] = Spell(
		name="Catapult",
		description='''Choose one object weighing 1 to 5 pounds within range that isn't being worn or carried. The object flies in a straight line up to 90 feet in a direction you choose before falling to the ground, stopping early if it impacts against a solid surface. If the object would strike a creature, that creature must make a Dexterity saving throw. On a failed save, the object strikes the target and stops moving. When the object strikes something, the object and what it strikes each take 3d8 bludgeoning damage.

At Higher Levels.
When you cast this spell using a spell slot of 2nd level or higher, the maximum weight of objects that you can target with this spell increases by 5 pounds, and the damage increases by 1d8, for each slot level above 1st.''',
		school="Transmutation",
		level=1,
		cast_time="1 action",
		range="60 ft",
		somatic=True,
		duration="Instantaneous")

	context.character.features["Features & Traits"]["Telekinetic"] = '''You learn to move things with your mind, granting you the following benefits:

Increase your Intelligence, Wisdom, or Charisma by 1, to a maximum of 20.

You learn the mage hand cantrip. You can cast it without verbal or somatic components, and you can make the spectral hand invisible. If you already know this spell, its range increases by 30 feet when you cast it. Its spellcasting ability is the ability increased by this feat.

As a bonus action, you can try to telekinetically shove one creature you can see within 30 feet of you. When you do so, the target must succeed on a Strength saving throw (DC 8 + your proficiency bonus + the ability modifier of the score increased by this feat) or be moved 5 feet toward you or away from you. A creature can willingly fail this save.'''
	context.character.int += 1
	context.character.features["Spellbook"]["Mage Hand"].range = "60 ft"

def update(context):
	pass