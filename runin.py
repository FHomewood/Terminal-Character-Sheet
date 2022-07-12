from sheet_variables import *
def init(context):
	context.character.int += 17
	context.character.str +=  8
	context.character.wis += 13
	context.character.con += 13
	context.character.dex += 14
	context.character.cha += 10

	context.character.race = "Half Elf"
	context.character.cha += 2
	context.character.int += 1
	context.character.con += 1
	context.character.spd = 30
	context.character.features["Features & Traits"]["Racial Traits"]["Darkvision"] = '''Thanks to your elf blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.'''
	context.character.features["Features & Traits"]["Racial Traits"]["Fey Ancestry"] = '''You have advantage on saving throws against being charmed, and magic can’t put you to sleep.'''
	context.character.features["Features & Traits"]["Racial Traits"]["Trance"] = '''Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.'''
	context.character.skill_proficiencies += ["Perception", "Insight"]
	context.character.features["Proficiencies"]["Languages"]["Common"] = None
	context.character.features["Proficiencies"]["Languages"]["Elvish"] = None
	context.character.features["Proficiencies"]["Languages"]["Dwarvish"] = None

	context.character.max_hp += 6 + 2
	context.character.background = "Orphan Loner"
	context.character.skill_proficiencies += ["Persuasion", "Investigation"]
	context.character.features["Proficiencies"]["Tools"]["Poisoners Kit"] = None
	context.character.features["Proficiencies"]["Languages"]["Draconic"] = None

	context.character.features["Spellbook"]['Toll the Dead'] = Spell(
		name='Toll the Dead',
		description= '''You point at one creature you can see within range, and the sound of a dolorous bell fills the air around it for a moment. The target must succeed on a Wisdom saving throw or take 1d8 necrotic damage. If the target is missing any of its hit points, it instead takes 1d12 necrotic damage.

The spell's damage increases by one die when you reach 5th level (2d8 or 2d12), 11th level (3d8 or 3d12), and 17th level (4d8 or 4d12).''',
		school= 'Necromancy' ,
		level= 0 ,
		cast_time= '1 Action' ,
		range= '60ft' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Instantaneous'
	)
	context.character.features["Spellbook"]['Chill Touch'] = Spell(
		name='Chill Touch',
		description= '''You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can't regain hit points until the start of your next turn. Until then, the hand clings to the target.

If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.

This spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).''',
		school= 'Necromancy' ,
		level= 0 ,
		cast_time= '1 Action' ,
		range= '120ft' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= '1 Round'
	)
	context.character.features["Spellbook"]['Message'] = Spell(
		name='Message',
		description= '''You point your finger toward a creature within range and whisper a message. The target (and only the target) hears the message and can reply in a whisper that only you can hear.

You can cast this spell through solid objects if you are familiar with the target and know it is beyond the barrier. Magical silence, 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the spell. The spell doesn't have to follow a straight line and can travel freely around corners or through openings.''',
		school= 'Transmutation' ,
		level= 0 ,
		cast_time= '1 Action' ,
		range= '120ft' ,
		verbal= True ,
		somatic= True ,
		material= "A short piece of copper wire" ,
		duration= '1 Round'
	)
	context.character.features["Spellbook"]['Mage Armour'] = Spell(
		name='Mage Armour',
		description= '''You touch a willing creature who isn’t wearing armor, and a protective magical force surrounds it until the spell ends. The target’s base AC becomes 13 + its Dexterity modifier. The spell ends if the target dons armor or if you dismiss the spell as an action.''',
		school= 'Abjuration' ,
		level= 1 ,
		cast_time= '1 action' ,
		range= 'Touch' ,
		verbal= True ,
		somatic= True ,
		material= True ,
		duration= '8 hours'
	)
	context.character.features["Spellbook"]['Sleep'] = Spell(
		name='Sleep',
		description= '''This spell sends creatures into a magical slumber. Roll 5d8; the total is how many hit points of creatures this spell can affect. Creatures within 20 feet of a point you choose within range are affected in ascending order of their current hit points (ignoring unconscious creatures).

Starting with the creature that has the lowest current hit points, each creature affected by this spell falls unconscious until the spell ends, the sleeper takes damage, or someone uses an action to shake or slap the sleeper awake. Subtract each creature's hit points from the total before moving on to the creature with the next lowest hit points. A creature's hit points must be equal to or less than the remaining total for that creature to be affected.

Undead and creatures immune to being charmed aren't affected by this spell.

At Higher Levels.
When you cast this spell using a spell slot of 2nd level or higher, roll an additional 2d8 for each slot level above 1st.''',
		school= 'Enchantment' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= '90ft' ,
		verbal= True ,
		somatic= True ,
		material= "A pinch of fine sand, rose petals, or a cricket" ,
		duration= '1 Minute'
	)
	context.character.features["Spellbook"]['False Life'] = Spell(
		name='False Life',
		description= '''Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4 temporary hit points for the duration.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you gain 5 additional temporary hit points for each slot level above 1st.''',
		school= 'Necromancy' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= 'Self' ,
		verbal= True ,
		somatic= True ,
		material= "A small amount of alcohol or distilled spirits" ,
		duration= '1 Hour'
	)
	context.character.features["Spellbook"]['Ray of Sickness'] = Spell(
		name='Ray of Sickness',
		description= '''A ray of sickening greenish energy lashes out toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 2d8 poison damage and must make a Constitution saving throw. On a failed save, it is also poisoned until the end of your next turn.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.''',
		school= 'Necromancy' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= '60ft' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Instantaneous'
	)
	context.character.features["Spellbook"]['Caustic Brew'] = Spell(
		name='Caustic Brew',
		description= '''A stream of acid emanates from you in a line 30 feet long and 5 feet wide in a direction you choose. Each creature in the line must succeed on a Dexterity saving throw or be covered in acid for the spell's duration or until a creature uses its action to scrape or wash the acid off itself or another creature. A creature covered in the acid takes 2d4 acid damage at start of each of its turns.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 2d4 for each slot level above 1st.''',
		school= 'Evocation' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= 'Self (30ft-line)' ,
		verbal= True ,
		somatic= True ,
		material= "A bit of rotten food" ,
		duration= 'Concentration, up to 1 minute'
	)
	context.character.features["Spellbook"]['Unseen Servant'] = Spell(
		name='Unseen Servant',
		description= '''This spell creates an invisible, mindless, shapeless, Medium force that performs simple tasks at your command until the spell ends. The servant springs into existence in an unoccupied space on the ground within range. It has AC 10, 1 hit point, and a Strength of 2, and it can't attack. If it drops to 0 hit points, the spell ends.

Once on each of your turns as a bonus action, you can mentally command the servant to move up to 15 feet and interact with an object. The servant can perform simple tasks that a human servant could do, such as fetching things, cleaning, mending, folding clothes, lighting fires, serving food, and pouring wine. Once you give the command, the servant performs the task to the best of its ability until it completes the task, then waits for your next command.

If you command the servant to perform a task that would move it more than 60 feet away from you, the spell ends.''',
		school= 'Conjuration' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= '60ft' ,
		verbal= True ,
		somatic= True ,
		material= "A piece of string and a bit of wood" ,
		duration= '1 Hour'
	)


	context.character.level = 2
	context.character.max_hp += 6 + 2
	context.character.features["Features & Traits"]["Class Features"]["Grim Harvest"] = """At 2nd level, you gain the ability to reap life energy from creatures you kill with your spells. Once per turn when you kill one or more creatures with a spell of 1st level or higher, you regain hit points equal to twice the spell's level, or three times its level if the spell belongs to the School of Necromancy. You don't gain this benefit for killing constructs or undead."""
	context.character.features["Spellbook"]['Charm Person'] = Spell(
		name='Charm Person',
		description= '''You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, and does so with advantage if you or your companions are fighting it. If it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it. The charmed creature regards you as a friendly acquaintance. When the spell ends, the creature knows it was charmed by you.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.''',
		school= 'Enchantment' ,
		level= 1 ,
		cast_time= '1 Action' ,
		range= '30ft' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= '1 Hour'
	)
	context.character.features["Spellbook"]['Expedious Release'] = Spell(
		name='Expedious Release',
		description= '''This spell allows you to move at an incredible pace. When you cast this spell, and then as a bonus action on each of your turns until the spell ends, you can take the Dash action.''',
		school= 'Transmutation' ,
		level= 1 ,
		cast_time= '1 Bonus Action' ,
		range= 'Self' ,
		verbal= True ,
		somatic= True ,
		material= False ,
		duration= 'Concentration, up to 10 minute'
	)

	context.character.level = 3
	context.character.max_hp += 6 + 2
	context.character.features["Spellbook"]["Cause Fear"] = Spell(
		name="Cause Fear",
		description='''You awaken the sense of mortality in one creature you can see within range. A construct or an undead is immune to this effect. The target must succeed on a Wisdom saving throw or become frightened of you until the spell ends. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.
At Higher Levels.

When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.''',
		school="Necromancy",
		level=1,
		cast_time="1 action",
		range="60 ft",
		verbal=True,
		concentration=True,
		duration="Up to 1 minute")
	context.character.features["Spellbook"]["Shield"] = Spell(
		name="Shield",
		description='''An invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from magic missile.''',
		school="Abjuration",
		level=1,
		cast_time="1 reaction",
		range="Self",
		verbal=True,
		somatic=True,
		duration='1 round')

	context.character.level = 4
	context.character.max_hp += 6 + 2
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
	context.character.features["Spellbook"]["Web"] = Spell(
		name="Web",
		description='''You conjure a mass of thick, sticky webbing at a point of your choice within range. The webs fill a 20-foot cube from that point for the duration. The webs are difficult terrain and lightly obscure their area.

If the webs aren't anchored between two solid masses (such as walls or trees) or layered across a floor, wall, or ceiling, the conjured web collapses on itself, and the spell ends at the start of your next turn. Webs layered over a flat surface have a depth of 5 feet.

Each creature that starts its turn in the webs or that enters them during its turn must make a Dexterity saving throw. On a failed save, the creature is restrained as long as it remains in the webs or until it breaks free.

A creature restrained by the webs can use its action to make a Strength check against your spell save DC. If it succeeds, it is no longer restrained.

The webs are flammable. Any 5-foot cube of webs exposed to fire burns away in 1 round, dealing 2d4 fire damage to any creature that starts its turn in the fire.''',
		school="Conjuration",
		level=2,
		cast_time="1 action",
		range="60 ft",
		verbal=True,
		somatic=True,
		material="a bit of spiderweb",
		concentration = True,
		duration="Up to 1 hour")
	context.character.features["Spellbook"]["Levitate"] = Spell(
		name="Levitate",
		description='''One creature or loose object of your choice that you can see within range rises vertically, up to 20 feet, and remains suspended there for the duration. The spell can levitate a target that weighs up to 500 pounds. An unwilling creature that succeeds on a Constitution saving throw is unaffected.

The target can move only by pushing or pulling against a fixed object or surface within reach (such as a wall or a ceiling), which allows it to move as if it were climbing. You can change the target's altitude by up to 20 feet in either direction on your turn. If you are the target, you can move up or down as part of your move. Otherwise, you can use your action to move the target, which must remain within the spell's range.

When the spell ends, the target floats gently to the ground if it is still aloft.''',
		school="Transmutation",
		level=2,
		cast_time="1 action",
		range="60 ft",
		verbal=True,
		somatic=True,
		material="small leather loop",
		concentration=True,
		duration="Up to 10 minutes")
	context.character.int += 2


def update(context):
	pass