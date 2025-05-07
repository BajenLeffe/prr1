'''
project3RPS.py: program där man spelar sten sax påse mot en "AI"

__author__  = "Alessandro Muller"
__version__ = "1.0.0"
__email__   = "alessandro.muller@elev.ga.ntig.se"
'''

"""
importera moduler

clear screen

dictionary med alla ASCII ikonerna{}

funktion som genererar nummer från 1-3:

funktion som enbart visar startskärmen:

funktion som tar emot spelarens val och jämför med datorns val:

funktion som visar statistiken:




"""

import random
from msvcrt import getwch
import os

os.system('cls')

ASCIIchar = {
    "R":"""
    _________
   |   |  |  \__
   /¨¨¨¨===  |  |
  /    ___/__|__|
 |    /         |
  \____ROCK_____/
""",
    "S":"""
  __       __
  \  \   /  /
   \  \ /  /
    \  V  /__ __
   /¨¨¨¨===  |  |
  /    ___/__|__|
 |    /         |
  \__SCISSORS___/

""",
    "P":"""
     __ __ __
    |  |  |  |__
    |¨¨|¨¨|¨¨|  |
 __ |¨¨|¨¨|¨¨|¨¨|
 \ \|  |  |  |¨¨|
 |  \__         |
 |              |
  \____PAPER____/

"""
}

def show_start_screen():
    os.system('cls')
    print("=== Välkommen till STEN SAX PÅSE ===")
    print("Tryck: R = Rock, P = Paper, S = Scissors")
    print("       N = Nytt spel, Q = Avsluta")
    print("====================================")

