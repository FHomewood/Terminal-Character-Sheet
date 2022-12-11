import TerminalCharacterSheet as tcs

def roll_stats(c):
    c.strength = 9
    c.dexterity = 16
    c.constitution = 16
    c.intelligence = 13
    c.wisdom = 14
    c.charisma = 17

def set_up(context):
    c = context.character

    roll_stats(c)
    sheet_layout(c)


    c.name = "Corrin TossCobble"
    c.alignment = "Lawful Good"
    c.gender = 'Male'


    c.race = "Lightfoot Halfling"
    c.size = 'Small (3\'½\")'
    c.weight = 'Light (44lbs)'
    c.age = 25
    c.speed = 25
    c.dexterity += 2
    c.charisma += 1
    c.features["Proficiencies"]["Languages"]["Common"] = """"""
    c.features["Proficiencies"]["Languages"]["Halfling"] = """"""
    c.features["Features & Traits"]["Racial Traits"]["Lucky"] = \
        """When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll."""
    c.features["Features & Traits"]["Racial Traits"]["Brave"] = \
        """You have advantage on saving throws against being frightened."""
    c.features["Features & Traits"]["Racial Traits"]["Halfling Nimbleness"] = \
        """You can move through the space of any creature that is of a size larger than yours."""
    c.features["Features & Traits"]["Racial Traits"]["Naturally Stealthy"] = \
        """You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."""


    c.character_class = "Bard"
    c.level = 1
    c.hit_dice = '1d8'
    c.proficiency_bonus = 2
    c.saving_throws = ["Dexterity", "Charisma"]
    c.skill_proficiencies = ['Deception', 'Intimidation', 'Performance']
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
    c.features["Proficiencies"]["Tools"]["Lute"] = \
        """"""
    c.features["Proficiencies"]["Tools"]["Viol"] = \
        """"""
    c.features["Proficiencies"]["Tools"]["Flute"] = \
        """"""
    c.features["Features & Traits"]["Class Features"]["Bardic Inspiration"] = \
        """You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6.

Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.

You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.

Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level."""
    c.features["Features & Traits"]["Class Features"]["Spellcasting"] = \
        """You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations. See Spells Rules for the general rules of spellcasting and the Spells Listing for the bard spell list.

        You can use a musical instrument (see the Tools section) as a spellcasting focus for your bard spells."""


    c.background = "Stone Mason Guild Artisan"
    c.skill_proficiencies += ['Insight', 'Perception']
    c.features["Proficiencies"]["Tools"]["Mason's Tools"] = \
    """"""
    c.features["Proficiencies"]["Languages"]["Gnomish"] = """"""
    c.features["Inventory"]["Equipment"]["Aleira"] = tcs.Item()


def sheet_layout(c):

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

def mod(skill):
    return int((skill - 10) / 2)


def assign_variables(context):
    c = context.character

    c.add_string('Character Name', c.name)
    c.add_string('Class', c.character_class)
    c.add_string('Level', f"{c.level:02}")
    c.add_string('Proficiency Bonus', f"{c.proficiency_bonus:+2}", (5, 2))
    c.add_string('Strength', f"{c.strength:02}", (3, 2))
    c.add_string('Strength', f"{mod(c.strength):+2}", (3, 3))
    c.add_string('Dexterity', f"{c.dexterity:02}", (3, 2))
    c.add_string('Dexterity', f"{mod(c.dexterity):+2}", (3, 3))
    c.add_string('Constitution', f"{c.constitution:02}", (3, 2))
    c.add_string('Constitution', f"{mod(c.constitution):+2}", (3, 3))
    c.add_string('Intelligence', f"{c.intelligence:02}", (3, 2))
    c.add_string('Intelligence', f"{mod(c.intelligence):+2}", (3, 3))
    c.add_string('Wisdom', f"{c.wisdom:02}", (3, 2))
    c.add_string('Wisdom', f"{mod(c.wisdom):+2}", (3, 3))
    c.add_string('Charisma', f"{c.charisma:02}", (3, 2))
    c.add_string('Charisma', f"{mod(c.charisma):+2}", (3, 3))
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

    c.add_string("Strength Saving Throw", f"{mod(c.strength):+2}", (5, 0))
    c.add_string("Dexterity Saving Throw", f"{mod(c.dexterity) + c.proficiency_bonus:+2}", (5, 0))
    c.add_string("Constitution Saving Throw", f"{mod(c.constitution):+2}", (5, 0))
    c.add_string("Intelligence Saving Throw", f"{mod(c.intelligence):+2}", (1, 0))
    c.add_string("Wisdom Saving Throw", f"{mod(c.wisdom):+2}", (1, 0))
    c.add_string("Charisma Saving Throw", f"{mod(c.charisma) + c.proficiency_bonus:+2}", (1, 0))

    c.add_string("Armour Class", f"{11 + mod(c.dexterity):02}", (4, 3))
    c.add_string("Initiative", f"{mod(c.dexterity):+2}", (6, 3))
    c.add_string("Speed", c.speed, (4, 3))

    context.modules["Icosahedron"].function = tcs.roll(c,1,20)

    context.modules["Acrobatics"].function = tcs.roll(c,1,20,mod(c.dexterity))
    context.modules["Animal Handling"].function = tcs.roll(c,1,20,mod(c.wisdom))
    context.modules["Arcana"].function = tcs.roll(c,1,20,mod(c.intelligence))
    context.modules["Athletics"].function = tcs.roll(c,1,20,mod(c.strength))
    context.modules["Deception"].function = tcs.roll(c,1,20,mod(c.charisma))
    context.modules["History"].function = tcs.roll(c,1,20,mod(c.intelligence))
    context.modules["Insight"].function = tcs.roll(c,1,20,mod(c.wisdom))
    context.modules["Intimidation"].function = tcs.roll(c,1,20,mod(c.charisma))
    context.modules["Investigation"].function = tcs.roll(c,1,20,mod(c.intelligence))
    context.modules["Medicine"].function = tcs.roll(c,1,20,mod(c.wisdom))
    context.modules["Nature"].function = tcs.roll(c,1,20,mod(c.intelligence))
    context.modules["Perception"].function = tcs.roll(c,1,20,mod(c.wisdom))
    context.modules["Performance"].function = tcs.roll(c,1,20,mod(c.charisma))
    context.modules["Persuasion"].function = tcs.roll(c,1,20,mod(c.charisma))
    context.modules["Religion"].function = tcs.roll(c,1,20,mod(c.intelligence))
    context.modules["Sleight of Hand"].function = tcs.roll(c,1,20,mod(c.dexterity))
    context.modules["Stealth"].function = tcs.roll(c,1,20,mod(c.dexterity))
    context.modules["Survival"].function = tcs.roll(c,1,20,mod(c.wisdom))

    context.modules["Strength Saving Throw"].function = tcs.roll(c,1,20,mod(c.strength))
    context.modules["Dexterity Saving Throw"].function = tcs.roll(c,1,20,mod(c.dexterity))
    context.modules["Constitution Saving Throw"].function = tcs.roll(c,1,20,mod(c.constitution))
    context.modules["Intelligence Saving Throw"].function = tcs.roll(c,1,20,mod(c.intelligence))
    context.modules["Wisdom Saving Throw"].function = tcs.roll(c,1,20,mod(c.wisdom))
    context.modules["Charisma Saving Throw"].function = tcs.roll(c,1,20,mod(c.charisma))

if __name__ == "__main__":
    corrin_tosscobble = tcs.Character()
    corrin_tosscobble.add_function(set_up, trigger='before')
    corrin_tosscobble.add_function(assign_variables, trigger='during')
    corrin_tosscobble.enable_dynamic_features()
    corrin_tosscobble.Display()
