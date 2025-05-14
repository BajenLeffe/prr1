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

huvudloop med allt:
  printa statistik varje gång():
  



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

stats= {'wins': 0, 'losses': 0, 'draws': 0, 'total': 0}

def start_screen():
    os.system('cls')
    print("=== Welcome to Rock Paper Scissors! ===")
    print("Tryck: R = Rock, P = Paper, S = Scissors")
    print("       N = New game, Q = Quit")
    print("====================================")

def show_stats(stats):
    print("\n=== Statistics ===")
    print(f"Won: {stats['wins']}")
    print(f"Lost: {stats['losses']}")
    print(f"Tie: {stats['draws']}")
    print(f"Total rounds: {stats['total']}")
    print("=================")

def computer_choice():
    return random.choice(['R', 'P', 'S'])

def show_result(player, computer):
  if player == computer:
    return 'draw!'
  
  elif (player == 'R' and computer == 'S') or\
    (player == 'P' and computer == 'R') or\
    (player == 'S' and computer == 'P'):
      return 'win!'
  
  else:
    return 'loss!'
 
os.system('cls')

start_screen()



