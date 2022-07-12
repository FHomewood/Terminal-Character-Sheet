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

class Character:
	def __init__(self):
		self.name = ""
		self.alignment = ""
		self._class = ""

		self.int = 0
		self.str = 0
		self.wis = 0
		self.con = 0
		self.dex = 0
		self.cha = 0

		self.max_hp = 0
		self.xp = 0
		self.wealth = 0

		self.features = {}
		self.skill_proficiencies = []

class Item:
	def __init__(self, name=None,description=None,weight=None,value=None, quantity=1):
		self.name = name
		self.description = description
		self.weight = weight
		self.value = value
		self.quantity = quantity

class Spell:
	def __init__(self,
		name=None,description=None,school=None,level=None,cast_time=None,
		range=None,concentration=None,ritual=None,verbal=None,somatic=None,
		material=None,duration=None,function=None):
			self.name = name
			self.description = description
			self.school = school
			self.level = level
			self.cast_time = cast_time
			self.range = range
			self.concentration = concentration
			self.ritual = ritual
			self.verbal = verbal
			self.somatic =somatic
			self.material = material
			self.duration = duration
			self.function = function

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
{                         }
{                         }
{                         }
{                         }
 '----------------------' """)
	context.art_blocks["STR Saving Throw"] = InteractiveBlock( (22,13), 3, 
		""" STR    """)
	context.art_blocks["DEX Saving Throw"] = InteractiveBlock( (23,13), 3, 
		""" DEX    """)
	context.art_blocks["CON Saving Throw"] = InteractiveBlock( (24,13), 3, 
		""" CON    """)
	context.art_blocks["INT Saving Throw"] = InteractiveBlock( (22,29), 3, 
		"""    INT """)
	context.art_blocks["WIS Saving Throw"] = InteractiveBlock( (23,29), 3, 
		"""    WIS """)
	context.art_blocks["CHA Saving Throw"] = InteractiveBlock( (24,29), 3, 
		"""    CHA """)
	context.art_blocks["Icosahedron"] = InteractiveBlock( (21,21), 3,
		""" .:/\\:.  
:\\/20\\/:
:/\\``/\\:
`._\\/_.' """)
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
	context.art_blocks["Initiative"] = InteractiveBlock( (14, 53) , 4,
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
	context.art_blocks["Hit Points"] = InteractiveBlock( (20, 42) , 1,
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
	context.art_blocks["Features Box"].scroll = 0

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

	context.art_blocks["Coin Pouch"] = InteractiveBlock( (45, 66) , 6,
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
	context.art_blocks["Casting"] = InteractiveBlock( (25, 44) , 4,
		""" CASTING  
          
          
          """)
	context.art_blocks["Attack Roll"] = InteractiveBlock( (25, 55) , 4,
		""" ATTACK ROLL 
             
             
             """)
	context.art_blocks["Spell Save DC"] = InteractiveBlock( (25, 69) , 4,
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
	context.art_blocks["Popup"].scroll=0
	context.art_blocks["Popup"].text=""
	context.art_blocks["Popup"].render=False
	context.art_blocks["Popup"].active=False



def neatify_string(context,string, splitlen=48):
	chunks = []
	while string != '':
		if len(string) >= splitlen:
			trial_chunk = ' '.join( string[0:splitlen].split(' ')[0:-1] )
			if '\n' in trial_chunk:
				trial_chunk = trial_chunk.split('\n')[0]
			string = string[len(trial_chunk)+1:]
		else:
			trial_chunk = string
			string = ''
		chunks.append(trial_chunk)
	return chunks

def feature_box_select(context, line_index):
	def func(context):
		current_headings = list(context.get_current_feature().keys())
		scroll_offset = context.art_blocks["Features Box"].scroll
		if mouse_event(context) == "Double Left Click":

			if line_index < len(current_headings)-scroll_offset:
				selected_heading = list(context.get_current_feature().keys())[line_index+scroll_offset]
				selected_attribute = context.get_current_feature()[selected_heading]
				if type(selected_attribute) == dict:
					context.feature_box_keys.append(selected_heading)
					context.art_blocks["Features Box"].scroll = 0
				elif type(selected_attribute) == str:
					string = selected_attribute
					popup_text = f""" 
   {selected_heading}
 
"""
					for line in neatify_string(context,string):
						popup_text +=f" {line}\n"
					activate_popup(context,popup_text)
				elif type(selected_attribute) == Spell:
					spell = selected_attribute
					popup_text = f""" 
  {spell.name}
  Level {spell.level} {spell.school}
  
  Cast Time: {spell.cast_time}
  Range: {spell.range}
  Duration: {spell.duration}
  {"V" * bool(spell.verbal)}{"S" * bool(spell.somatic)}{"M" * bool(spell.material)}              {"C" * bool(spell.concentration)} {"R" * bool(spell.ritual)}
                ~~~~~~~~~~~~~~~~~

"""
					for line in neatify_string(context,spell.description):
						popup_text +=f" {line}\n"
					activate_popup(context,popup_text)
				elif type(selected_attribute) == Item:
					item = selected_attribute
					popup_text = f""" 
  {item.name} x{item.quantity}

  {item.weight} lbs
  {item.value} cp
                ~~~~~~~~~~~~~~~~~
 
"""
					for line in neatify_string(context,item.description):
						popup_text +=f" {line}\n"
					activate_popup(context,popup_text)
		if mouse_event(context) in ["Right Click", "Double Right Click"]:
			context.feature_box_keys = context.feature_box_keys[:-1]
			context.art_blocks["Features Box"].scroll = 0
		if mouse_event(context) == "Scroll Up":
			context.art_blocks["Features Box"].scroll = max(0, context.art_blocks["Features Box"].scroll - 1)
		if mouse_event(context) == "Scroll Down":
			context.art_blocks["Features Box"].scroll = min(context.art_blocks["Features Box"].scroll+1, len(current_headings)-1)

	return func

def roll(context,n,k,b):
	def func(context):
		if mouse_event(context) =="Double Left Click":
			rv = sum([numpy.random.randint(1,20)]) + b
			context.art_blocks["Icosahedron"].var_array = [[22,24,f'{rv:02}']]
	return func

def popup_function(context):
	if "Right" in mouse_event(context):
		for index, block in context.art_blocks.items():
			if block.render: block.active = True
		context.mouse_state = (0,0,0,0,0)
		context.art_blocks["Popup"].render = False
		context.art_blocks["Popup"].active = False
	if "Scroll Up" in mouse_event(context):
		context.art_blocks["Popup"].scroll = max(0,context.art_blocks["Popup"].scroll - 1)
	if "Scroll Down" in mouse_event(context):
		context.art_blocks["Popup"].scroll = min(len(context.art_blocks["Popup"].text.split("\n"))-3, context.art_blocks["Popup"].scroll + 1)
	update_popup(context)

def activate_popup(context, text=None):
	for index, block in context.art_blocks.items():
		block.active = False
	context.art_blocks["Popup"].render = True
	context.art_blocks["Popup"].active = True
	context.art_blocks["Popup"].text = text
	context.art_blocks["Popup"].scroll = 0
	update_popup(context)


def update_popup(context):
	text = context.art_blocks["Popup"].text
	scroll_offset = context.art_blocks["Popup"].scroll
	temp_var_array = [[0,50,f'{scroll_offset}']]
	line_number = 0
	for paragraph in text.split('\n'):
		for chunk in [paragraph[i:i+49] for i in range(0,len(paragraph), 49)]:
			temp_var_array += [[line_number - scroll_offset + 20,16,chunk]]
			line_number+=1
	scroll_offset = min(len(temp_var_array),scroll_offset)
	context.art_blocks["Popup"].var_array = temp_var_array[scroll_offset+1:scroll_offset+20]


def get_mouse(context):
	old_mouse_state = list(context.mouse_state)
	new_mouse_state = list(curses.getmouse())

	for attribute in range(len(new_mouse_state)):
		if new_mouse_state[attribute] < 0:
			new_mouse_state[attribute] = old_mouse_state[attribute]
	context.mouse_state = tuple(new_mouse_state)

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
		65536: 'Scroll Up',
		2097152: 'Scroll Down',
	}[code]
	except:
		return str(code)
