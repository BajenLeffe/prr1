'''
project2besties.py: program som man lägger till, ändrar eller tar bort personer/kompisar

__author__  = "Alessandro Muller"
__version__ = "1.0.0"
__email__   = "alessandro.muller@elev.ga.ntig.se"
'''

import os 
from colors import bcolors


"""
funktion som tar emot namn:
    append namn till lista

funktion som tar bort namn:
    if sats som hittar vilket namn som ska tas bort:
        remove namn från lista

funktion som ändrar namn:
    if sats som hittar vilket namn som ska ändras:
        ändra namnet som ska ändras

lista för namnen

huvudloop:
    inre loop
        clear screen


        for-loop som skriver ut alla namn i ordning:
        
        input som låter användaren välja vad hen vill göra med namnen

        if och elif satser baserade på vad användaren vill göra

        fråga om användaren vill avsluta eller fortsätta
"""

def addnamelist(list, first): #funktion för att lägga till namn
    
    list.append(first)

def removenamelist(list, index): #funktion för att ta bort namn
    if 0 <= index < len(list): #kollar efter om användaren har angett ett relevant nummer för namnet i listan som ska bort

        list.pop(index)

def editnamelist(name_list, oldfirst, newfirst): #funktion för att ändra namn
    if 0 <= index < len(name_list):  #hittar vilket index/nummer namnet har

        name_list[index] = newfirst  #byter ut med nya namnet

    
namelist = [] #här läggs alla namn till

while True:
    while True:
        os.system('cls') #rensar skärmen så att det inte blir klottrat
        print("=" * 90)

        print(bcolors.PURPLE+"\nCurrent list:"+bcolors.DEFAULT)

        for i, name in enumerate(namelist, start=1): #visar aktuell lista med nummer
            print(f"{i}: {name}")
        
        print(f"\namount of names: {len(namelist)}") #visar antal namn i listan

        
        print("\nDo you want to \nA. Add a name \nB. Remove a name \nC. Change a name \nD. End? ")

        print("=" * 90)

        choice = input("\nEnter your choice from A-D: ").lower() #här får användaren bestämma vad hen vill göra
        

        if choice == "a": #om användaren vill lägga till ett namn tas hen till denna del
            name = input(bcolors.CYAN+"Give a name to add: "+bcolors.DEFAULT)

            addnamelist(namelist, name)

        elif choice == "b": #om användaren vill ta bort ett namn tas hen till denna del
            try:
                index = int(input(bcolors.YELLOW + "Give the number of the name to be removed: " + bcolors.DEFAULT)) -1
                removenamelist(namelist, index)
            except:
                print(bcolors.RED + "Please enter a valid number." + bcolors.DEFAULT)
 
        elif choice == "c": #om användaren vill ändra ett namn tas hen till denna del
            try: #kollar om man har skrivit rätt
                index = int(input("Which number do you want to change?: ")) - 1
            except: #om man har skrivit fel
                print(bcolors.RED + "Please enter a valid number." + bcolors.DEFAULT)

            if 0 <= index < len(namelist):
                    newname = input("Enter the new name: ")
                    editnamelist(namelist, index, newname)
            else:
                    print(bcolors.RED + "Invalid number. Please select a valid number from the list." + bcolors.DEFAULT)

            
        elif choice == "d": #om användaren vill avsluta programmet tas hen till denna del
            print(bcolors.RED+"Ending program...."+bcolors.DEFAULT)
            exit()

        else: #om användaren råkar skriva fel tas hen till denna del
            print(bcolors.RED+"Wrong choice."+bcolors.DEFAULT)

