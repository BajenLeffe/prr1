
import os
from random import randint
from colors import bcolors
from time import sleep


while True:
    os.system("cls")
    print("buffering")
    for i in range(randint(1, 5)):
        for period in range(1,5):
            sleep(0.3)
            os.system("cls")
            print("buffering", "." * period)
    os.system("cls")

    os.system('cls')
    print("=" * 90)
    print(bcolors.PURPLE+"Welcome to the game of Guess the number (1-100)!" "\n" "You get 7 tries! Go ahead!" "\n" "wanna quit? press 0"+bcolors.DEFAULT) #bcolors är en hjälpklass för att lägga färger på text i programmet

    tries = 1
    number = randint(1,100) #väljer ett random tal mellan 1-100

    while tries <= 7:
        print("tries: ", tries)

        try:
            guess = int(input("Put your guess here!: ")) #här gissar man
        except:
            print(bcolors.RED+"You sure that you put in a number there pal?"+bcolors.DEFAULT) #finns i fall någon skriver en bokstav
            continue

        if guess == 0:
            print("calling it quits?")
            break
        
        elif guess > number:
            print(bcolors.CYAN+"Your guess is larger than the real number!"+bcolors.DEFAULT) #om man gissar för högt

        elif guess < number:
            print(bcolors.CYAN+"your guess is too low!"+bcolors.DEFAULT) #om man gissar för lågt

        elif guess == number:
            print(bcolors.GREEN+"YAY YOU GOT IT!"+bcolors.DEFAULT) #om man får rätt
            break
        
        tries += 1 #tickar på variabeln med 1 så den bryts efter 5 försök

    if tries == 8:
        yesno = str(input(bcolors.BLUE+"sorry! you lost! try again? (Y/N): "+bcolors.DEFAULT)).upper() #finns om mer än 7 försök har gjorts

    else:    
        yesno = str(input(bcolors.GREEN+"\n" "yay! you finished the game! try again? (Y/N): "+bcolors.DEFAULT)).upper() #om man vinner

    if yesno in ["NO","N"]:
        print(bcolors.BOLD+"See you some other time!"+bcolors.DEFAULT) #hejdå meddelande om man vill inte fortsätta
        os.system("cls")
        print("exiting")
        for i in range(randint(1, 5)):
            for period in range(1,5):
                sleep(0.3)
                os.system("cls")
                print("exiting", "." * period)
        os.system("cls")
        break
    
    else:
        continue

        
        



