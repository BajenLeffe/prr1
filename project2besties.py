'''
project2besties.py: program som man lägger till, ändrar eller tar bort personer

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
    if 0 <= index < len(list):
        list.pop(index)

def editnamelist(name_list, oldfirst, newfirst): #funktion för att ändra namn
    try:
        index = name_list.index(oldfirst)  #hittar vilket index/nummer namnet har
        name_list[index] = newfirst  #byter ut med nya namnet
    except:
        print("Name does not exist") #error i fall andvändaren råkar skriva fel

    
namelist = [] #här läggs alla namn till

while True:
    while True:
        os.system('cls') #rensar skärmen så att det inte blir klottrat
        
        print(bcolors.PURPLE + "\nAktuell lista:" + bcolors.DEFAULT)
        for i, name in enumerate(namelist): #visar aktuell lista
            print(f"{i}: {name}")

        print("=" * 90)
        choice = input("\nDo you want to [A]dd, [R]emove, [C]hange a name or [E]nd? ").lower() #här får användaren bestämma vad hen vill göra

        if choice == "a": #om användaren vill lägga till ett namn tas hen till denna del
            name = input("Give a name to add: ")
            addnamelist(namelist, name)
        elif choice == "r": #om användaren vill ta bort ett namn tas hen till denna del
            try:
                index = int(input("Give the index of the name to be removed: "))
                removenamelist(namelist, index)
            except: #finns för att förhindra error eller krasch
                print("please enter a number")
        elif choice == "c": #om användaren vill ändra ett namn tas hen till denna del
            oldname = input("Which name do you want to change?: ")
            newname = input("Enter the new name: ")
            editnamelist(namelist, oldname, newname)
        elif choice == "e": #om användaren vill avsluta programmet tas hen till denna del
            print("Ending program.")
            break
        else: #om användaren råkar skriva fel tas hen till denna del
            print("Wrong choice.")
