import TerminalCharacterSheet as tcs


def set_up(context):
    c = context.character

    c.name = "Corrin TossCobble"
    c.alignment = "Lawful Neutral"
    c.race = "Rock Gnome"
    c.speed = 30

    c.character_class = "Bard"
    c.level = 1

    c.hit_dice = '1d8'
    c.proficiency_bonus = 2
    c.saving_throws = ["Dexterity", "Charisma"]

    c.strength = 8
    c.dexterity = 14
    c.constitution = 13
    c.intelligence = 15
    c.wisdom = 10
    c.charisma = 15

    c.skill_proficiencies = [
        'Acrobatics', 'Deception', 'Perception',
        'Performance', 'Sleight of Hand'
    ]

    c.features = \
        {
            "Proficiencies": {
                "Weapons & Armour": {},
                "Tools": {},
                "Languages": {}
            },
            "Features & Traits": {
                "Racial Traits": {},
                "Class Features": {}
            },
            "Inventory": {
                "Equipment": {},
                "Backpack": {},
                "Treasures": {}
            },
            "Spellbook": {}
        }
    c.features["Features & Traits"]["Racial Traits"]["Darkvision"] = \
        """Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."""
    c.features["Features & Traits"]["Racial Traits"]["Gnome Cunning"] = \
        """You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."""
    c.features["Features & Traits"]["Racial Traits"]["Artificers Lore"] = \
        """Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply."""
    c.features["Features & Traits"]["Racial Traits"]["Tinker"] = \
        """You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time.
When you create a device, choose one of the following options:

Clockwork Toy.
This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.

Fire Starter.
The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.

Music Box.
When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.
"""
    c.features["Features & Traits"]["Class Features"]["Bardic Inspiration"] = \
        """You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6.

Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.

You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.

Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level."""
    c.features["Proficiencies"]["Weapons & Armour"]["Light Armour"] = \
        """Light armor is favored by bards because it lets them make the best use of their Dexterity and doesn't interfere with performances. When you wear light armor, you add your Dexterity modifier to the number shown on the table to determine your Armor Class."""
    c.features["Proficiencies"]["Weapons & Armour"]["Simple Weapons"] = \
        """In times of desperation many adventurers can depend on simple weapons to carry then when their main weapon is out of commission
        
        Simple Weapons include:
        
        - Club
        - Dagger
        - Greatclub
        - Handaxe
        - Javelin
        - Lighthammer
        - Mace
        - Quarterstaff
        - Spear
        - Light Crossbow
        - Shortbow"""
    c.features["Proficiencies"]["Weapons & Armour"]["Hand crossbows"] = \
        """"""
    c.features["Proficiencies"]["Weapons & Armour"]["Longswords"] = \
        """"""
    c.features["Proficiencies"]["Weapons & Armour"]["Rapiers"] = \
        """"""
    c.features["Proficiencies"]["Weapons & Armour"]["Shortswords"] = \
        """"""


def mod(skill):
    return int((skill - 10) / 2)


def assign_variables(context):
    c = context.character

    c.add_string('Character Name', c.name)
    c.add_string('Class', c.character_class)
    c.add_string('Level', f"{c.level:02}")
    c.add_string('Proficiency Bonus', f"{c.proficiency_bonus:+2}", (5, 2))
    c.add_string('STR', f"{c.strength:02}", (3, 2))
    c.add_string('STR', f"{mod(c.strength):+2}", (3, 3))
    c.add_string('DEX', f"{c.dexterity:02}", (3, 2))
    c.add_string('DEX', f"{mod(c.dexterity):+2}", (3, 3))
    c.add_string('CON', f"{c.constitution:02}", (3, 2))
    c.add_string('CON', f"{mod(c.constitution):+2}", (3, 3))
    c.add_string('INT', f"{c.intelligence:02}", (3, 2))
    c.add_string('INT', f"{mod(c.intelligence):+2}", (3, 3))
    c.add_string('WIS', f"{c.wisdom:02}", (3, 2))
    c.add_string('WIS', f"{mod(c.wisdom):+2}", (3, 3))
    c.add_string('CHA', f"{c.charisma:02}", (3, 2))
    c.add_string('CHA', f"{mod(c.charisma):+2}", (3, 3))
    c.add_string('Passive Perception', f"{10 + mod(c.wisdom) + c.proficiency_bonus:02}", (3, 3))

    for skill in c.skill_proficiencies:
        c.add_string(skill, '*', (1, 0))

    c.add_string("Acrobatics", f"{mod(c.dexterity) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("Animal Handling", f"{mod(c.wisdom):+2}", (24, 0))
    c.add_string("Arcana", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("Athletics", f"{mod(c.strength):+2}", (24, 0))
    c.add_string("Deception", f"{mod(c.charisma) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("History", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("Insight", f"{mod(c.wisdom):+2}", (24, 0))
    c.add_string("Intimidation", f"{mod(c.charisma):+2}", (24, 0))
    c.add_string("Investigation", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("Medicine", f"{mod(c.wisdom):+2}", (24, 0))
    c.add_string("Nature", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("Perception", f"{mod(c.wisdom) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("Performance", f"{mod(c.charisma) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("Persuasion", f"{mod(c.charisma):+2}", (24, 0))
    c.add_string("Religion", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("Sleight of Hand", f"{mod(c.dexterity) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("Stealth", f"{mod(c.dexterity):+2}", (24, 0))
    c.add_string("Survival", f"{mod(c.wisdom):+2}", (24, 0))

    c.add_string("STR Saving Throw", f"{mod(c.strength):+2}", (5, 0))
    c.add_string("DEX Saving Throw", f"{mod(c.dexterity) + c.proficiency_bonus:+2}", (5, 0))
    c.add_string("CON Saving Throw", f"{mod(c.constitution):+2}", (5, 0))
    c.add_string("INT Saving Throw", f"{mod(c.intelligence):+2}", (1, 0))
    c.add_string("WIS Saving Throw", f"{mod(c.wisdom):+2}", (1, 0))
    c.add_string("CHA Saving Throw", f"{mod(c.charisma) + c.proficiency_bonus:+2}", (1, 0))

    c.add_string("Armour Class", f"{11 + mod(c.dexterity):02}", (4, 3))
    c.add_string("Initiative", f"{mod(c.dexterity):+2}", (6, 3))
    c.add_string("Speed", c.speed, (4, 3))

if __name__ == "__main__":
    corrin_tosscobble = tcs.Character()
    corrin_tosscobble.add_function(set_up, trigger='before')
    corrin_tosscobble.add_function(assign_variables, trigger='during')
    corrin_tosscobble.enable_dynamic_features()
    corrin_tosscobble.Display()
