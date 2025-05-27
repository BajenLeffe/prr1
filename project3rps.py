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

  if och elif satser baserat på vad användaren har skrivit:
  
  else i fall användarens val är fel:
  
  



"""

import random
from msvcrt import getwch
import os
from colors import bcolors

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

while True:
    print("\nYour choice (R/P/S), N to restart, Q to quit:")
    choice = getwch().upper()

    if choice in ['R', 'P', 'S']:
        os.system('cls')
        computer = computer_choice()
        result = show_result(choice, computer)
        stats['total'] += 1

        print(bcolors.GREEN+"\nYou chose:"+bcolors.DEFAULT)
        print(bcolors.GREEN+ASCIIchar[choice]+bcolors.DEFAULT)
        print(bcolors.RED+"The AI chose:"+bcolors.DEFAULT)
        print(bcolors.RED+ASCIIchar[computer]+bcolors.DEFAULT)

        if result == 'win!':
            stats['wins'] += 1
            print(bcolors.GREEN+"YOU WON!"+bcolors.DEFAULT)

        elif result == 'loss!':
            stats['losses'] += 1
            print(bcolors.RED+"YOU LOST!"+bcolors.DEFAULT)

        else:
            stats['draws'] += 1
            print(bcolors.YELLOW+"IT'S A DRAW!"+bcolors.DEFAULT)

        show_stats(stats)

    elif choice == 'Q':
        print(bcolors.BLUE+"\nYou better play again!! I spent way too much time working on this!"+bcolors.DEFAULT)
        break

    elif choice == 'N':
        stats = {'wins': 0, 'losses': 0, 'draws': 0, 'total': 0}
        start_screen()

    
    else:
        print(bcolors.RED+"Invalid option ya dog, CHOOSE AGAIN!"+bcolors.DEFAULT)


