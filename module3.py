import os
os.system('cls')

"""age = int(input("please enter your age: "))
if age >= 18:
    print("you can go to the pub!")

else:
    print("you're too young! wait until you're 18! haha!")

if age == 18:
    print('you are exactly old enough to go to the pub')

elif age > 18:
    print("you're above 18!")

elif age == 17:
    print("i'm sorry bro")

elif age < 15:
    print("MINOR ALERT! GET LOST!")

elif age == 15:
    print("meeeeeh, i'm iffy about you..")"""

baldur_online = True

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




