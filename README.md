<!-- Copyright 2022 Frankie Homewood -->

# Terminal Character Sheet

TCS is a Python package that provides an interface to create and dynamically create your own programmable charactersheet.

Born of a homebrewing experiment gone right. TCS was created after Finding that there are few options for creating character sheets for those truly game-breaking characters that require a turing complete set of tools in order to describe them accurately. 

TCS provides users with the ability to generate characters according to standard 5e rules or inject their own personal ruleset for their characters.


## Setup

### Installation

The public TCS repository is hosted via [GitHub](https://github.com/FHomewood/Terminal-Character-Sheet/) where the source code can be accessed within the restrictions of the LICENSE file.

Stable scheduled releases of TCS binary installers are avaiable through the [Python Package Index (PyPI)](https://pypi.org/project/terminal-character-sheet/)

```
$ pip install terminal-character-sheet
```

the package is then accessible as any other python package 
```
### ./Corrin_TossCobble.py

import TerminalCharacterSheet as tcs

...
```
### Development

The supplementary directories for testing, examples, etc. will not by default have TCS in their PYTHONPATH, to enable the scripts in these directories add this to your python path by either installing the PyPI package or adding the root directory to the PYTHONPATH in your virtual environment

```
### /venv/Lib/site-packages/_virtualenv.py 

PROJECT_ROOT_DIR = ...
sys.path.append(PROJECT_ROOT_DIR)

...
```
