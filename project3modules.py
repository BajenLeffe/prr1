import random
from msvcrt import getwch
import os
from colors import bcolors

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

def start_screen():
    os.system('cls')
    print(bcolors.PURPLE+"=== Welcome to Rock Paper Scissors! ===")
    print("Tryck: R = Rock, P = Paper, S = Scissors")
    print("       N = New game, Q = Quit")
    print("===================================="+bcolors.DEFAULT)

def show_stats(stats):
    print(bcolors.CYAN+"\n=== Statistics ===")
    print(f"Won: {stats['wins']}")
    print(f"Lost: {stats['losses']}")
    print(f"Tie: {stats['draws']}")
    print(f"Total rounds: {stats['total']}")
    print("================="+bcolors.DEFAULT)

def computer_choice():
    return random.choice(['R', 'P', 'S']) #här väljer datorn mellan sten, sax och påse med random

def show_result(player, computer):
  if player == computer:
    return 'draw!'
  
  elif (player == 'R' and computer == 'S') or\
    (player == 'P' and computer == 'R') or\
    (player == 'S' and computer == 'P'): #samlade ihop alla dessa för att slippa lägga in en massa elif-satser
    return 'win!'
  
  else:
    return 'loss!'