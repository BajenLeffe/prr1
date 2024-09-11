import os
from random import randint
from math import pi
os.system('cls')

print("=" * 90)

while True:
    try:
        age = int(input("please enter your age: "))
        if age >= 18:
            print("you can go to the pub!")
            

        else:
            print("you're too young! wait until you're 18! haha!")
            break

        if age == 18:
            print('you are exactly old enough to go to the pub')
            break

        elif age > 18:
            print("you're over 18! GO NUTS")
            break

        elif age == 17:
            print("i'm sorry bro")
            break

        elif age < 15:
            print("MINOR ALERT! GET LOST!")
            break

        elif age == 15:
            print("meeeeeh, i'm iffy about you..")
            break
    except:
        print("please.. for the love of god put in a number...")
        continue

baldur_online = True

print("=" * 90)

if baldur_online:
    while True:
        try:
            height = float(input("height (in M): "))
            break
        except: 
            print("you goober, put in your height! IN NUMBERS MAN")
            continue
    
    if height >= 1.2 and height <= 1.99:
        print("you can ride baldur!")
    elif height >= 2.00:
        print("bro, we don't fit skyscrapers here! GO HOME!")
    else:
        print("ya short fuc, GO HOME!")
else: 
    print("we're closed man, come back later!")

print("=" * 90)

print("random numbers until they reach 6!")

random_number = 0

while random_number != 6:
    random_number = randint(1,6)
    print(random_number)

print("=" * 90)
print("you're going to measure the area of a circle!")

pi = pi

while True:
    try:
        radius = float(input("please enter a radius (in cm): "))
        break
    except:
        print("please, for the love of god, put in a number PLEASE")
        continue

area = pi * radius**2
 
print("\n", f'the total area of the circle given is: {area} cm^2')

print("=" * 90)
print("dice roll time!")


while True:
    try:
        amount = int(input("please enter amount of rolls you want: "))
        break
    except:
        print("ENTER A NUMBER, HOW MANY TIMES DO I HAVE TO TELL YOU?!")
        continue

counter = amount

while counter > 0:
    dice = randint(1,6)
    print(dice)
    counter -= 1
