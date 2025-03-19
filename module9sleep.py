import os
from random import randint
from colors import bcolors
from time import sleep
from msvcrt import getwch

while True:
    os.system("cls")
    print("buffering")
    for i in range(randint(1, 5)):
        for period in range(1, 5):
            sleep(0.3)
            os.system("cls")
            print("buffering", "." * period)
    os.system("cls")

    os.system('cls')
    print("=" * 90)
    print(bcolors.PURPLE+"Welcome to the game of Guess the number (1-100)!" "\n" "You get 7 tries! Go ahead!" "\n" "wanna quit? press 0"+bcolors.DEFAULT)

    tries = 1
    number = randint(1, 100)

    while tries <= 7:
        print("tries: ", tries)

        try:
            guess = ""
            while not guess.isdigit():
                char = getwch()
                if char == "\r":  # Enter key pressed
                    break
                elif char.isdigit():
                    guess += char
                elif char == "\x1b":  # Escape key to quit
                    guess = "0"
                    break
            
            guess = int(guess)
        except:
            print(bcolors.RED+"You sure that you put in a number there pal?"+bcolors.DEFAULT)
            continue

        if guess == 0:
            print("calling it quits?")
            break
        
        elif guess > number:
            print(bcolors.CYAN+"Your guess is larger than the real number!"+bcolors.DEFAULT)

        elif guess < number:
            print(bcolors.CYAN+"your guess is too low!"+bcolors.DEFAULT)

        elif guess == number:
            print(bcolors.GREEN+"YAY YOU GOT IT!"+bcolors.DEFAULT)
            break
        
        tries += 1

    if tries == 8:
        print(bcolors.BLUE+"sorry! you lost! try again? (Y/N): "+bcolors.DEFAULT, end="", flush=True)
        yesno = getwch().upper()
    else:
        print(bcolors.GREEN+"\n" "yay! you finished the game! try again? (Y/N): "+bcolors.DEFAULT, end="", flush=True)
        yesno = getwch().upper()

    if yesno in ["N"]:
        print(bcolors.BOLD+"See you some other time!"+bcolors.DEFAULT)
        os.system("cls")
        print("exiting")
        for i in range(randint(1, 5)):
            for period in range(1, 5):
                sleep(0.3)
                os.system("cls")
                print("exiting", "." * period)
        os.system("cls")
        break
