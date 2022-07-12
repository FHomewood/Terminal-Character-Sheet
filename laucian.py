from sheet_variables import *
def init(context):
	context.character.int += 16
	context.character.str += 11
	context.character.wis += 14
	context.character.con += 16
	context.character.dex +=  3
	context.character.cha += 11

	context.character.race = "Elf"
	context.character.dex += 2
	context.character.spd = 30
	context.character.features["Features & Traits"]["Racial Traits"]["Darkvision"] = '''Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.'''
	context.character.features["Features & Traits"]["Racial Traits"]["Fey Ancestry"] = '''Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.'''
	context.character.features["Features & Traits"]["Racial Traits"]["Trance"] = '''Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.'''
	context.character.skill_proficiencies += ['Perception']
	context.character.features["Proficiencies"]["Languages"]["Common"] = None
	context.character.features["Proficiencies"]["Languages"]["Elvish"] = None

	context.character.subrace = "High Elf"
	context.character.int += 1
	context.character.features["Proficiencies"]["Weapons"]["Longsword"] = None
	context.character.features["Proficiencies"]["Weapons"]["Shortsword"] = None
	context.character.features["Proficiencies"]["Weapons"]["Longbow"] = None
	context.character.features["Proficiencies"]["Weapons"]["Shortbow"] = None
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
	context.character.features["Proficiencies"]["Languages"]["Orcish"] = None

	context.character.max_hp += 6 + 3

	context.character.background = "Reclusive Herbalist"
	context.character.skill_proficiencies += ["Medicine", "Nature"]
	context.character.features["Proficiencies"]["Tools"]["Herbalism Kit"] = None
	context.character.features["Proficiencies"]["Tools"]["Lyre"] = None

	context.character.features["Spellbook"]['Light'] = Spell(
		name='Light',
		school= 'Evocation' ,
		level= 0 ,
		cast_time= '1 action' ,
		range= 'Touch' ,
		verbal= True ,
		somatic= False ,
		material= True ,
		duration= '1 hour' ,
		description= '''You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like. Completely covering the object with something opaque blocks the light. The spell ends if you cast it again or dismiss it as an action.
If you target an object held or worn by a hostile creature, that creature must succeed on a Dexterity saving throw to avoid the spell.'''
	)
	context.character.features["Spellbook"]['Fire Bolt'] = Spell(
		name='Fire Bolt',
		school= 'Evocation' ,
		level= 0 ,
		cast_time= '1 action' ,
		range= '120ft' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Instantaneous' ,
		description= '''You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn’t being worn or carried.
At Higher Levels. This spell’s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10).'''
	)
	context.character.features["Spellbook"]['Prestidigitation'] = Spell(
		name='Prestidigitation',
		school= 'Transmutation' ,
		level= 0 ,
		cast_time= '1 Action' ,
		range= '10ft' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Up to 1 hour' ,
		description= '''This spell is a minor magical trick that novice spellcasters use for practice. You create one of the following magical effects within range:

* You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor.

* You instantaneously light or snuff out a candle, a torch, or a small campfire.

* You instantaneously clean or soil an object no larger than 1 cubic foot.

* You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour.

* You make a color, a small mark, or a symbol appear on an object or a surface for 1 hour.

* You create a nonmagical trinket or an illusory image that can fit in your hand and that lasts until the end of your next turn.

If you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action.'''
	)
	context.character.features["Spellbook"]['Mage Armour'] = Spell(
		name='Mage Armour',
		school= 'Abjuration' ,
		level= 1 ,
		cast_time= '1 action' ,
		range= 'Touch' ,
		verbal= True ,
		somatic= True ,
		material= True ,
		duration= '8 hours' ,
		description= '''You touch a willing creature who isn’t wearing armor, and a protective magical force surrounds it until the spell ends. The target’s base AC becomes 13 + its Dexterity modifier. The spell ends if the target dons armor or if you dismiss the spell as an action.'''
	)
	context.character.features["Spellbook"]['Find Familiar'] = Spell(
		name='Find Familiar',
		school= 'Conjuration' ,
		level= 1 ,
		cast_time= '1 hour' ,
		range= '10ft' ,
		verbal= True ,
		somatic= True ,
		material= True ,
		duration= 'Instantaneous' ,
		description= '''You gain the service of a familiar, a spirit that takes an animal form you choose: bat, cat, crab, frog (toad), hawk, lizard, octopus, owl, poisonous snake, fish (quipper), rat, raven, sea horse, spider, or weasel. Appearing in an unoccupied space within range, the familiar has the statistics of the chosen form, though it is a celestial, fey, or fiend (your choice) instead of a beast.

Your familiar acts independently of you, but it always obeys your commands. In combat, it rolls its own initiative and acts on its own turn. A familiar can’t attack, but it can take other actions as normal.

When the familiar drops to 0 hit points, it disappears, leaving behind no physical form. It reappears after you cast this spell again. As an action, you can temporarily dismiss your familiar to a pocket dimension. Alternatively, you can dismiss it forever. As an action while it is temporarily dismissed, you can cause it to reappear in any unoccupied space within 30 feet of you. Whenever the familiar drops to 0 hit points or disappears into the pocket dimension, it leaves behind in its space anything it was wearing or carrying.

While your familiar is within 100 feet of you, you can communicate with it telepathically. Additionally, as an action, you can see through your familiar’s eyes and hear what it hears until the start of your next turn, gaining the benefits of any special senses that the familiar has. During this time, you are deaf and blind with regard to your own senses.

You can’t have more than one familiar at a time. If you cast this spell while you already have a familiar, you instead cause it to adopt a new form. Choose one of the forms from the above list. Your familiar transforms into the chosen creature.

Finally, when you cast a spell with a range of touch, your familiar can deliver the spell as if it had cast the spell. Your familiar must be within 100 feet of you, and it must use its reaction to deliver the spell when you cast it. If the spell requires an attack roll, you use your attack modifier for the roll.'''
	)
	context.character.features["Spellbook"]['Alarm'] = Spell(
		name='Alarm',
		school= 'Abjuration' ,
		level= 1 ,
		cast_time= '1 action' ,
		range= '30ft' ,
		verbal= True ,
		somatic= True ,
		material= True ,
		duration= '8 hours' ,
		description= '''You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won’t set off the alarm. You also choose whether the alarm is mental or audible.

A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping. An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.'''
	)
	context.character.features["Spellbook"]['Burning Hands'] = Spell(
		name='Burning Hands',
		school= 'Evocation' ,
		level= 1 ,
		cast_time= '1 action' ,
		range= 'Self (15ft cone)' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Instantaneous' ,
		description= '''As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one.

The fire ignites any flammable objects in the area that aren’t being worn or carried.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.'''
	)
	context.character.features["Spellbook"]['Shield'] = Spell(
		name='Shield',
		school= 'Abjuration' ,
		level= 1 ,
		cast_time= '1 reaction, which you take when you are hit by an attack or targeted my the Magic Missile spell' ,
		range= 'Self' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= '1 round' ,
		description= '''An invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from Magic Missile.'''
	)
	context.character.features["Spellbook"]['Thunderwave'] = Spell(
		name='Thunderwave',
		school= 'Evocation' ,
		level= 1 ,
		cast_time= '1 action' ,
		range= 'Self (15ft cube)' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Instantaneous' ,
		description= '''A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube originating from you must make a Constitution saving throw. On a failed save, a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a successful save, the creature takes half as much damage and isn’t pushed.

In addition, unsecured objects that are completely within the area of effect are automatically pushed 10 feet away from you by the spell’s effect, and the spell emits a thunderous boom audible out to 300 feet.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.'''
	)

	context.character.level = 2
	context.character.max_hp += 4 + 2
	context.character.features["Features & Traits"]["Class Features"]["Arcane Ward"] = """Starting at 2nd level, you can weave magic around yourself for protection. When you cast an abjuration spell of 1st level or higher, you can simultaneously use a strand of the spell's magic to create a magical ward on yourself that lasts until you finish a long rest. The ward has a hit point maximum equal to twice your wizard level + your Intelligence modifier. Whenever you take damage, the ward takes the damage instead. If this damage reduces the ward to 0 hit points, you take any remaining damage.
While the ward has 0 hit points, it can't absorb damage, but its magic remains. Whenever you cast an abjuration spell of 1st level or higher, the ward regains a number of hit points equal to twice the level of the spell.
Once you create the ward, you can't create it again until you finish a long rest."""
	context.character.features["Spellbook"]['Floating Disk'] = Spell(
		name='Floating Disk',
		school= 'Conjuration' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= '30ft' ,
		verbal= True ,
		somatic= True ,
		material= 'A drop of mercury' ,
		duration= '1 Hour' ,
		description= '''This spell creates a circular, horizontal plane of force, 3 feet in diameter and 1 inch thick, that floats 3 feet above the ground in an unoccupied space of your choice that you can see within range. The disk remains for the duration, and can hold up to 500 pounds. If more weight is placed on it, the spell ends, and everything on the disk falls to the ground.

The disk is immobile while you are within 20 feet of it. If you move more than 20 feet away from it, the disk follows you so that it remains within 20 feet of you. It can move across uneven terrain, up or down stairs, slopes and the like, but it can't cross an elevation change of 10 feet or more. For example, the disk can't move across a 10-foot-deep pit, nor could it leave such a pit if it was created at the bottom.

If you move more than 100 feet from the disk (typically because it can't move around an obstacle to follow you), the spell ends.'''
	)
	context.character.features["Spellbook"]['Detect Magic'] = Spell(
		name='Detect Magic',
		school= 'Divination' ,
		level= 1 ,
		cast_time= '1 action' ,
		range= 'Self' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Concentration, up to 10 minutes' ,
		description= '''For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.'''
	)

	context.character.level = 3
	context.character.max_hp += 4 + 3
	context.character.features["Spellbook"]["Arcane Lock"] = Spell(
		name="Arcane Lock",
		description='''You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. You and the creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute. Otherwise, it is impassable until it is broken or the spell is dispelled or suppressed. Casting knock on the object suppresses arcane lock for 10 minutes.

While affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.''',
		school="Abjuration",
		level=2,
		cast_time="1 action",
		range="Touch",
		verbal=True,
		somatic=True,
		material="25gp of gold dust",
		duration="Until dispelled")
	context.character.features["Spellbook"]["Maximillian's Earthen Grasp"] = Spell(
		name="Maximillian's Earthen Grasp",
		description='''You choose a 5-foot-square unoccupied space on the ground that you can see within range. A Medium hand made from compacted soil rises there and reaches for one creature you can see within 5 feet of it. The target must make a Strength saving throw. On a failed save, the target takes 2d6 bludgeoning damage and is restrained for the spell's duration.

As an action, you can cause the hand to crush the restrained target, which must make a Strength saving throw. The target takes 2d6 bludgeoning damage on a failed save, or half as much damage on a successful one.

To break out, the restrained target can use its action to make a Strength check against your spell save DC. On a success, the target escapes and is no longer restrained by the hand.

As an action, you can cause the hand to reach for a different creature or to move to a different unoccupied space within range. The hand releases a restrained target if you do either.''',
		school="Transmutation",
		level=2,
		cast_time="1 action",
		range="30 ft",
		verbal=True,
		somatic=True,
		material="a minature hand sculpted from clay",
		concentration=True,
		duration="Up to 1 minute")

	context.character.level = 4
	context.character.max_hp += 4 + 3
	context.character.features["Spellbook"]["Absorb Elements"] = Spell(
		name="Absorb Elements",
		description='''The spell captures some of the incoming energy, lessening its effect on you and storing it for your next melee attack. You have resistance to the triggering damage type until the start of your next turn. Also, the first time you hit with a melee attack on your next turn, the target takes an extra 1d6 damage of the triggering type, and the spell ends.
At Higher Levels.

When you cast this spell using a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each slot level above 1st.''',
		school="Abjuration",
		level=1,
		cast_time="1 reaction",
		range="Self",
		somatic= True,
		duration="1 round")
	context.character.features["Spellbook"]["Feather Fall"] = Spell(
		name="Feather Fall",
		description='''Choose up to five falling creatures within range. A falling creature's rate of descent slows to 60 feet per round until the spell ends. If the creature lands before the spell ends, it takes no falling damage and can land on its feet, and the spell ends for that creature.''',
		school="Transmutation",
		level=1,
		cast_time="1 reaction",
		range="60 ft",
		verbal=True,
		material="a small feather",
		duration="1 minute")
	context.character.features["Spellbook"]["Create Bonfire"] = Spell(
		name="Create Bonfire",
		description='''You create a bonfire on ground that you can see within range. Until the spell ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire's space when you cast the spell must succeed on a Dexterity saving throw or take 1d8 fire damage. A creature must also make the saving throw when it moves into the bonfire's space for the first time on a turn or ends its turn there.

The bonfire ignites flammable objects in its area that aren't being worn or carried.

The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).''',
		school="Conjuration",
		level=0,
		cast_time="1 action",
		range="60 ft",
		verbal=True,
		somatic= True,
		concentration=True,
		duration="Up to 1 minute")
	context.character.features["Features & Traits"]["Lucky"] = '''You have inexplicable luck that seems to kick in at just the right moment.

You have 3 luck points. Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points after you roll the die, but before the outcome is determined. You choose which of the d20s is used for the attack roll, ability check, or saving throw.

You can also spend one luck point when an attack roll is made against you. Roll a d20, and then choose whether the attack uses the attacker's roll or yours. If more than one creature spends a luck point to influence the outcome of a roll, the points cancel each other out; no additional dice are rolled.

You regain your expended luck points when you finish a long rest.'''


def update(context):
	pass