import os
from random import randint
os.system('cls')

while True:
    prompt = input("give a number: ")
    
    if prompt.isdigit() == True:
        print("yay you gave a number")
        break

    elif prompt.isdigit() == False:
        print("try again pal")


number = randint(0,10)

while True:
    guess = input("guess a number between 0 and 10 or press Q to exit: ")

    if guess.upper() == "Q":
        break

    elif guess.isdigit() == False:
        print("you sure you put in the right number and/or pressed Q?")

    elif int(guess) == number:
        print("you did it!")
        break


    

