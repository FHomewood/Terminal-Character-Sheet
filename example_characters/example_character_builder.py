# Copyright 2022 Frankie Homewood

import terminal_character_sheet as tcs


if __name__ == "__main__":
    builder = tcs.CharacterBuilder()
    builder.InitializeSheet(layout="default") \
           .roll_stats() \
           .randomize_all(level=1) \
    character = builder.get_character()
    character.display()
