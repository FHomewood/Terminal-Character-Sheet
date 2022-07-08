import curses
import numpy

class InteractiveBlock:

	def __init__(self,pos,color,art):
		self.render = True
		self.active = True
		self.pos = pos
		self.color = color
		self.art = art
		self.var_array = []
		self.function = None

	def replace_in_string(self,y,x,val):
		line_array = self.art.split('\n')
		pre_change = line_array[:y-1]
		change_line = line_array[y]
		change_line = [change_line[:x] + val + change_line[x+len(val):]]
		post_change = line_array[y+1:]
		new_string = pre_change + change_line + post_change
		new_string = '\n'.join(new_string)
		return new_string

	def draw(self,context):
		if not self.render: return
		if self.mouse_in_block(context) and self.active:
			color = self.color
		else: color = 0

		for index, line in enumerate(self.art.split('\n')):
			context.stdscr.addstr(self.pos[0]+index,self.pos[1],line, curses.color_pair(color))
		for y, x, line in self.var_array:
			context.stdscr.addstr(y,x,line, curses.color_pair(color))

	def mouse_in_block(self,context):
		t = self.pos[0]
		l = self.pos[1]
		b = t + len(self.art.split('\n'))
		r = l + max([len(line) for line in self.art.split('\n')])-1

		x = context.mouse_state[1]
		y = context.mouse_state[2]

		return (x >= l and x <= r and y >= t and y < b)

def define_art_blocks(context):
	context.art_blocks["Header"] = InteractiveBlock( (1, 2) , 0,
		""".-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-.""")
	context.art_blocks["Banner"] = InteractiveBlock( (3, 1) , 0,
		"""         ,),,)
      \'     ',)
     ,`  ,--.  ',  ,                        
     :  /    }  G}'   DUNGEONS & DRAGONS  
    ',  \\    ',,V     5E CHARACTER SHEET   
    \\___\\_____;;l_____________________________________________________________
  _/          ';/                                                            \\\\ 
 //|                                                        -                 \\\\
// ;                       ,---.      ,                                       //
\\\\ \\______________________/  _  \\___,'/______________________________________//
 \\\\_'/            VZ\\  '  /  \\  .' /                                      
                  +FAR`.__,'    `.__,'""")
	context.art_blocks["Character Name"] = InteractiveBlock( (10, 21) , 3,
		"""                    """)
	context.art_blocks["Class"] = InteractiveBlock( (10, 54) , 3,
		"""      """)
	context.art_blocks["Level"] = InteractiveBlock( (10, 63) , 3,
		"""  """)
	context.art_blocks["STR"] = InteractiveBlock( (14, 1) , 4,
		"""/------\\
| STR: |
[      ]
[ (  ) ]
\\\\<''>//""")
	context.art_blocks["DEX"] = InteractiveBlock( (19, 1) , 4,
		"""/------\\
| DEX: |
[      ]
[ (  ) ]
\\~:><:~/""")
	context.art_blocks["CON"] = InteractiveBlock( (24, 1) , 4,
		"""/------\\
| CON: |
[      ]
[ (  ) ]
\\_\\()/_/""")
	context.art_blocks["INT"] = InteractiveBlock( (29, 1) , 4,
		"""/------\\
| INT: |
[      ]
[ (  ) ]
\\+/{}\\+/""")
	context.art_blocks["WIS"] = InteractiveBlock( (34, 1) , 4,
		"""/------\\
| WIS: |
[      ]
[ (  ) ]
\\+_/\\_+/""")
	context.art_blocks["CHA"] = InteractiveBlock( (39, 1) , 4,
		"""/------\\
| CHA: |
[      ]
[ (  ) ]
\\"}--{"/""")
	context.art_blocks["Passive Perception"] = InteractiveBlock( (44, 1) , 4,
		"""/------\\
| PAS. |
[ PER: ]
[      ]
\\::[]::/""")
	context.art_blocks["Proficiency Bonus"] = InteractiveBlock( (15, 10) , 0,
		""" .--------------------------. 
{                            }
{        PROFICIENCY BONUS   }
{                            }
 '--------------------------' """)
	context.art_blocks["Saving Throws"] = InteractiveBlock( (20, 12) , 0,
		""" .----------------------. 
{         .:/\\:.         }
{ STR    :\\/20\\/:    INT }
{ DEX    :/\\``/\\:    WIS }
{ CON    `._\\/_.'    CHA }
 '----------------------' """)
	context.art_blocks["Separator 1"] = InteractiveBlock( (26, 18) , 0,
		"""~~~~~~~~~~~~~~~~""")
	context.art_blocks["Skills Box"] = InteractiveBlock( (27, 10) , 0,
		""" .--------------------------. 
{           SKILLS           }
{                            }
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
{                            }
{                            }
 '--------------------------' """)
	context.art_blocks["Armour Class"] = InteractiveBlock( (14, 42) , 0,
		"""   _.._   
 _/    \\_ 
)   AC   (
|        |
 \\      / 
  '-..-'  """)
	context.art_blocks["Initiative"] = InteractiveBlock( (14, 53) , 0,
		""".------------.
|/          \\|
| INITIATIVE |
|            |
|\\          /|
'------------'""")
	context.art_blocks["Speed"] = InteractiveBlock( (14, 68) , 0,
		""".-----------.
|/         \\|
|   SPEED   |
|      ft   |
|\\         /|
'-----------'""")
	context.art_blocks["Hit Points"] = InteractiveBlock( (20, 42) , 0,
		""" .-----------------------------------.
{ HIT POINTS:                        }
{ TEMP HIT POINTS:                   }
 '-----------------------------------'""")
	context.art_blocks["Combat Stats"] = InteractiveBlock( (24, 42) , 0,
		""".-----------.-------------.-----------.
|/          #             #          \\|
|           #             #           |
|           #             #           |
|\\          #             #          /|
'-----------'-------------'-----------'""")
	context.art_blocks["Features Box"] = InteractiveBlock( (30, 42) , 0,
		""" .-----------------------------------.
{                                     }
{                                     }
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
|                                     ]
|                                     ]
|                                     ]
 '...................................'""")

	context.art_blocks["Features Line 0"] = InteractiveBlock( (32, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 0"].function = feature_box_select(context,0)

	context.art_blocks["Features Line 1"] = InteractiveBlock( (33, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 1"].function = feature_box_select(context,1)

	context.art_blocks["Features Line 2"] = InteractiveBlock( (34, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 2"].function = feature_box_select(context,2)

	context.art_blocks["Features Line 3"] = InteractiveBlock( (35, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 3"].function = feature_box_select(context,3)

	context.art_blocks["Features Line 4"] = InteractiveBlock( (36, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 4"].function = feature_box_select(context,4)

	context.art_blocks["Features Line 5"] = InteractiveBlock( (37, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 5"].function = feature_box_select(context,5)

	context.art_blocks["Features Line 6"] = InteractiveBlock( (38, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 6"].function = feature_box_select(context,6)

	context.art_blocks["Features Line 7"] = InteractiveBlock( (39, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 7"].function = feature_box_select(context,7)

	context.art_blocks["Features Line 8"] = InteractiveBlock( (40, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 8"].function = feature_box_select(context,8)

	context.art_blocks["Features Line 9"] = InteractiveBlock( (41, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 9"].function = feature_box_select(context,9)

	context.art_blocks["Features Line 10"] = InteractiveBlock( (42, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 10"].function = feature_box_select(context,10)

	context.art_blocks["Features Line 11"] = InteractiveBlock( (43, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 11"].function = feature_box_select(context,11)

	context.art_blocks["Features Line 12"] = InteractiveBlock( (44, 44) , 3,
		"""___________________________________""")
	context.art_blocks["Features Line 12"].function = feature_box_select(context,12)

	context.art_blocks["Features Line 13"] = InteractiveBlock( (45, 44) , 3,
		"""_______________________""")
	context.art_blocks["Features Line 13"].function = feature_box_select(context,13)

	context.art_blocks["Features Line 14"] = InteractiveBlock( (46, 44) , 3,
		"""______________________""")
	context.art_blocks["Features Line 14"].function = feature_box_select(context,14)

	context.art_blocks["Features Line 15"] = InteractiveBlock( (47, 44) , 3,
		"""______________________""")
	context.art_blocks["Features Line 15"].function = feature_box_select(context,15)

	context.art_blocks["Coin Pouch"] = InteractiveBlock( (45, 66) , 2,
		"""_.-----------<
[    P G S C  
[             """)
	context.art_blocks["Footer"] = InteractiveBlock( (50, 1) , 0,
		"""'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'""")
	context.art_blocks["Acrobatics"] = InteractiveBlock( (29, 11) , 6,
		"""   Acrobatics               """)
	context.art_blocks["Animal Handling"] = InteractiveBlock( (30, 11) , 6,
		"""   Animal Handling          """)
	context.art_blocks["Arcana"] = InteractiveBlock( (31, 11) , 6,
		"""   Arcana                   """)
	context.art_blocks["Athletics"] = InteractiveBlock( (32, 11) , 6,
		"""   Athletics                """)
	context.art_blocks["Deception"] = InteractiveBlock( (33, 11) , 6,
		"""   Deception                """)
	context.art_blocks["History"] = InteractiveBlock( (34, 11) , 6,
		"""   History                  """)
	context.art_blocks["Insight"] = InteractiveBlock( (35, 11) , 6,
		"""   Insight                  """)
	context.art_blocks["Intimidation"] = InteractiveBlock( (36, 11) , 6,
		"""   Intimidation             """)
	context.art_blocks["Investigation"] = InteractiveBlock( (37, 11) , 6,
		"""   Investigation            """)
	context.art_blocks["Medicine"] = InteractiveBlock( (38, 11) , 6,
		"""   Medicine                 """)
	context.art_blocks["Nature"] = InteractiveBlock( (39, 11) , 6,
		"""   Nature                   """)
	context.art_blocks["Perception"] = InteractiveBlock( (40, 11) , 6,
		"""   Perception               """)
	context.art_blocks["Performance"] = InteractiveBlock( (41, 11) , 6,
		"""   Performance              """)
	context.art_blocks["Persuasion"] = InteractiveBlock( (42, 11) , 6,
		"""   Persuasion               """)
	context.art_blocks["Religion"] = InteractiveBlock( (43, 11) , 6,
		"""   Religion                 """)
	context.art_blocks["Sleight of Hand"] = InteractiveBlock( (44, 11) , 6,
		"""   Sleight of Hand          """)
	context.art_blocks["Stealth"] = InteractiveBlock( (45, 11) , 6,
		"""   Stealth                  """)
	context.art_blocks["Survival"] = InteractiveBlock( (46, 11) , 6,
		"""   Survival                 """)
	context.art_blocks["Casting"] = InteractiveBlock( (25, 44) , 2,
		""" CASTING  
          
          
          """)
	context.art_blocks["Attack Roll"] = InteractiveBlock( (25, 55) , 2,
		""" ATTACK ROLL 
             
             
             """)
	context.art_blocks["Spell Save DC"] = InteractiveBlock( (25, 69) , 2,
		""" SPELL DC 
          
          
          """)

	context.art_blocks["Popup"] = InteractiveBlock( (17, 12) , 4,
		""" .-.------------------------------------------------.-.
((o))                                                  )
 \\U/_______          __________________          _____/
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |                                                 |
   |____    _______    _________________  ____    ___|
  /A\\                                                 \\
 ((o))                                                 )
  '-'-------------------------------------------------'""")
	context.art_blocks["Popup"].function=popup_function
	context.art_blocks["Popup"].render=False
	context.art_blocks["Popup"].active=False
	context.art_blocks["STR"].function = roll(context,1,20,2)


def feature_box_select(context, line_index):
	def func(context):
		if mouse_event(context) == "Double Left Click":
			current_headings = list(context.get_current_feature().keys())
			if line_index < len(current_headings):
				selected_heading = list(context.get_current_feature().keys())[line_index]
				context.feature_box_keys.append(selected_heading)
		if mouse_event(context) in ["Right Click", "Double Right Click"]:
			context.feature_box_keys = context.feature_box_keys[:-1]
	return func

def roll(context,n,k,b):
	def func(context):
		if mouse_event(context) =="Double Left Click":
			for index, block in context.art_blocks.items():
				block.active = False
			context.art_blocks["Popup"].render = True
			context.art_blocks["Popup"].active = True
			roll_val = sum([numpy.random.randint(1,20)]) + b
			context.art_blocks["Popup"].var_array=[
			[25,30,"        _-_."],
			[26,30,"     _-',^. `-_."],
			[27,30," ._-' ,'   `.   `-_ "],
			[28,30,"!`-_._________`-':::"],
			[29,30,"!   /\\        /\\::::"],
			[30,30,f";  /  \\  {roll_val:02}  /..\\:::"],
			[31,30,"! /    \\    /....\\::"],
			[32,30,"!/      \\  /......\\:"],
			[33,30,";--.___. \\/_.__.--;; "],
			[34,30," '-_    `:!;;;;;;;'"],
			[35,30,"    `-_, :!;;;''"],
			[36,30,"        `-!'"]

			]
	return func

def popup_function(context):
	if "Right" in mouse_event(context):
		for index, block in context.art_blocks.items():
			if block.render: block.active = True
		context.art_blocks["Popup"].render = False
		context.art_blocks["Popup"].active = False

def mouse_event(context):
	code = context.mouse_state[-1]
	try:
		return {
		0: 'None',
		1: 'Left Button Release',
		2: 'Left Button Press',
		4: 'Left Click',
		8: 'Double Left Click',
		32: 'Middle Button Release',
		64: 'Middle Button Press',
		128: 'Middle Click',
		256: 'Double Middle Click',
		1024: 'Right Button Release',
		2048: 'Right Button Press',
		4096: 'Right Click',
		8192: 'Double Right Click',
	}[code]
	except:
		return str(code)
