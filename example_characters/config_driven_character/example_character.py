# Copyright 2023 Frankie Homewood

import sys
PROJECT_ROOT_DIR = '/home/frankiehomewood/Development/Terminal-Character-Sheet/'
sys.path.append(PROJECT_ROOT_DIR)

import TerminalCharacterSheet as tcs
import TerminalCharacterSheet.utils as tcs_utils

import yaml
from pathlib import Path

def set_up(context):
    c = context.character

    with open(Path(__file__).parent/'character_stats.yml', 'r') as stats_file:
        stats = yaml.safe_load(stats_file)['stats']
    c.features = tcs_utils.combine_features([
        stats.pop('race features',dict()),
        stats.pop('class features',dict()),
        stats.pop('background features',dict())
    ])
    c.strength = int(stats.pop('strength',0)) + int(stats.pop('race strength',0))
    c.dexterity = int(stats.pop('dexterity',0)) + int(stats.pop('race dexterity',0))
    c.constitution = int(stats.pop('constitution',0)) + int(stats.pop('race constitution',0))
    c.intelligence = int(stats.pop('intelligence',0)) + int(stats.pop('race intelligence',0))
    c.wisdom = int(stats.pop('wisdom',0)) + int(stats.pop('race wisdom',0))
    c.charisma = int(stats.pop('charisma',0)) + int(stats.pop('race charisma',0))
    c.skill_proficiencies = c.features['proficiencies'].pop('skill proficiencies', list())
    for key in stats.keys():
        exec(f"c.{key} = stats['{key}']")


def mod(skill):
    return int((skill - 10) / 2)


def assign_variables(context):
    c = context.character

    c.add_string('character_name', c.name)
    c.add_string('character_class', c.character_class)
    c.add_string('level', f"{c.level:02}")
    c.add_string('proficiency_bonus', f"{c.proficiency_bonus:+2}", (5, 2))
    c.add_string('strength', f"{c.strength:02}", (3, 2))
    c.add_string('strength', f"{mod(c.strength):+2}", (3, 3))
    c.add_string('dexterity', f"{c.dexterity:02}", (3, 2))
    c.add_string('dexterity', f"{mod(c.dexterity):+2}", (3, 3))
    c.add_string('constitution', f"{c.constitution:02}", (3, 2))
    c.add_string('constitution', f"{mod(c.constitution):+2}", (3, 3))
    c.add_string('intelligence', f"{c.intelligence:02}", (3, 2))
    c.add_string('intelligence', f"{mod(c.intelligence):+2}", (3, 3))
    c.add_string('wisdom', f"{c.wisdom:02}", (3, 2))
    c.add_string('wisdom', f"{mod(c.wisdom):+2}", (3, 3))
    c.add_string('charisma', f"{c.charisma:02}", (3, 2))
    c.add_string('charisma', f"{mod(c.charisma):+2}", (3, 3))
    c.add_string('passive_perception', f"{10 + mod(c.wisdom) + c.proficiency_bonus:02}", (3, 3))

    for skill in c.skill_proficiencies:
        c.add_string(skill, '*', (1, 0))

    c.add_string("acrobatics", f"{mod(c.dexterity) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("animal_handling", f"{mod(c.wisdom):+2}", (24, 0))
    c.add_string("arcana", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("athletics", f"{mod(c.strength):+2}", (24, 0))
    c.add_string("deception", f"{mod(c.charisma) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("history", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("insight", f"{mod(c.wisdom):+2}", (24, 0))
    c.add_string("intimidation", f"{mod(c.charisma):+2}", (24, 0))
    c.add_string("investigation", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("medicine", f"{mod(c.wisdom):+2}", (24, 0))
    c.add_string("nature", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("perception", f"{mod(c.wisdom) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("performance", f"{mod(c.charisma) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("persuasion", f"{mod(c.charisma):+2}", (24, 0))
    c.add_string("religion", f"{mod(c.intelligence):+2}", (24, 0))
    c.add_string("sleight_of_hand", f"{mod(c.dexterity) + c.proficiency_bonus:+2}", (24, 0))
    c.add_string("stealth", f"{mod(c.dexterity):+2}", (24, 0))
    c.add_string("survival", f"{mod(c.wisdom):+2}", (24, 0))

    c.add_string("strength_saving_throw", f"{mod(c.strength):+2}", (5, 0))
    c.add_string("dexterity_saving_throw", f"{mod(c.dexterity) + c.proficiency_bonus:+2}", (5, 0))
    c.add_string("constitution_saving_throw", f"{mod(c.constitution):+2}", (5, 0))
    c.add_string("intelligence_saving_throw", f"{mod(c.intelligence):+2}", (1, 0))
    c.add_string("wisdom_saving_throw", f"{mod(c.wisdom):+2}", (1, 0))
    c.add_string("charisma_saving_throw", f"{mod(c.charisma) + c.proficiency_bonus:+2}", (1, 0))

    c.add_string("armour_class", f"{11 + mod(c.dexterity):02}", (4, 3))
    c.add_string("initiative", f"{mod(c.dexterity):+2}", (6, 3))
    c.add_string("speed", c.speed, (4, 3))

    context.modules["icosahedron"].function = tcs.roll(c, 1, 20)

    context.modules["acrobatics"].function = tcs.roll(c, 1, 20, mod(c.dexterity))
    context.modules["animal_handling"].function = tcs.roll(c, 1, 20, mod(c.wisdom))
    context.modules["arcana"].function = tcs.roll(c, 1, 20, mod(c.intelligence))
    context.modules["athletics"].function = tcs.roll(c, 1, 20, mod(c.strength))
    context.modules["deception"].function = tcs.roll(c, 1, 20, mod(c.charisma))
    context.modules["history"].function = tcs.roll(c, 1, 20, mod(c.intelligence))
    context.modules["insight"].function = tcs.roll(c, 1, 20, mod(c.wisdom))
    context.modules["intimidation"].function = tcs.roll(c, 1, 20, mod(c.charisma))
    context.modules["investigation"].function = tcs.roll(c, 1, 20, mod(c.intelligence))
    context.modules["medicine"].function = tcs.roll(c, 1, 20, mod(c.wisdom))
    context.modules["nature"].function = tcs.roll(c, 1, 20, mod(c.intelligence))
    context.modules["perception"].function = tcs.roll(c, 1, 20, mod(c.wisdom))
    context.modules["performance"].function = tcs.roll(c, 1, 20, mod(c.charisma))
    context.modules["persuasion"].function = tcs.roll(c, 1, 20, mod(c.charisma))
    context.modules["religion"].function = tcs.roll(c, 1, 20, mod(c.intelligence))
    context.modules["sleight_of_hand"].function = tcs.roll(c, 1, 20, mod(c.dexterity))
    context.modules["stealth"].function = tcs.roll(c, 1, 20, mod(c.dexterity))
    context.modules["survival"].function = tcs.roll(c, 1, 20, mod(c.wisdom))

    context.modules["strength_saving_throw"].function = tcs.roll(c, 1, 20, mod(c.strength))
    context.modules["dexterity_saving_throw"].function = tcs.roll(c, 1, 20, mod(c.dexterity))
    context.modules["constitution_saving_throw"].function = tcs.roll(c, 1, 20, mod(c.constitution))
    context.modules["intelligence_saving_throw"].function = tcs.roll(c, 1, 20, mod(c.intelligence))
    context.modules["wisdom_saving_throw"].function = tcs.roll(c, 1, 20, mod(c.wisdom))
    context.modules["charisma_saving_throw"].function = tcs.roll(c, 1, 20, mod(c.charisma))



if __name__ == "__main__":
    corrin_tosscobble = tcs.Character()
    corrin_tosscobble.add_function(set_up, trigger='before')
    corrin_tosscobble.add_function(assign_variables, trigger='during')
    corrin_tosscobble.enable_dynamic_features()
    corrin_tosscobble.Display()
