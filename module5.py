import os
from random import randint
os.system('cls')

print("=" * 90)

while True:
    prompt = input("give a number: ")
    
    if prompt.isdigit() == True:
        print("yay you gave a number")
        break

    elif prompt.isdigit() == False:
        print("try again pal")


number = randint(0,11)

print("=" * 90)

while True:
    guess = input("guess a number between 0 and 10 or press Q to exit: ")

    if guess.upper() == "Q":
        break

    elif guess.isdigit() == False:
        print("you sure you put in the right number and/or pressed Q?")

    elif int(guess) == number:
        print("you did it!")
        break

print("=" * 90)

string = "korkisligan"

print(string[:10])
    
string2 = input("give a short sentence: ")

print(string2[:10]+"...")