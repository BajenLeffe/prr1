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
(OBS! ALLA FUNKTIONER ÄR FLYTTADE TILL project3modules.py)

huvudloop med allt:
  printa statistik varje gång():

  if och elif satser baserat på vad användaren har skrivit:
  
  else i fall användarens val är fel:
  
  



"""

from msvcrt import getwch
import os
from colors import bcolors
import project3modules

os.system('cls')

stats= {'wins': 0, 'losses': 0, 'draws': 0, 'total': 0}
 
os.system('cls')

project3modules.start_screen()

while True:
    print("\nYour choice (R/P/S), N to restart, Q to quit:")
    choice = getwch().upper()

    if choice in ['R', 'P', 'S']:
        os.system('cls')
        project3modules.computer = project3modules.computer_choice()
        project3modules.result = project3modules.show_result(choice, project3modules.computer)
        stats['total'] += 1

        print(bcolors.GREEN+"\nYou chose:"+bcolors.DEFAULT)
        print(bcolors.GREEN+project3modules.ASCIIchar[choice]+bcolors.DEFAULT)
        print(bcolors.RED+"The AI chose:"+bcolors.DEFAULT)
        print(bcolors.RED+project3modules.ASCIIchar[project3modules.computer]+bcolors.DEFAULT)

        if project3modules.result == 'win!':
            stats['wins'] += 1
            print(bcolors.GREEN+"YOU WON!"+bcolors.DEFAULT)

        elif project3modules.result == 'loss!':
            stats['losses'] += 1
            print(bcolors.RED+"YOU LOST!"+bcolors.DEFAULT)

        else:
            stats['draws'] += 1
            print(bcolors.YELLOW+"IT'S A DRAW!"+bcolors.DEFAULT)

        project3modules.show_stats(stats)

    elif choice == 'Q':
        print(bcolors.BLUE+"\nYou better play again!! I spent way too much time working on this!"+bcolors.DEFAULT)
        break

    elif choice == 'N':
        stats = {'wins': 0, 'losses': 0, 'draws': 0, 'total': 0}
        project3modules.start_screen()

    
    else:
        print(bcolors.RED+"Invalid option ya dog, CHOOSE AGAIN!"+bcolors.DEFAULT)


