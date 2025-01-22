import os
os.system('cls')

def add(x, y):
    return x + y

def name():
    fname = input("First name: ")
    lname = input("Last name: ")
    print(f"Your name is {fname} {lname}")

def addnamelist(list, first):
    list.append(first)

def removenamelist(list, index):
    if 0 <= index < len(list):
        list.pop(index)

def editnamelist(list, oldfirst, newfirst):
    if oldfirst in list:
        index = list.index(oldfirst)
        list[index] = newfirst


    


def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

    else:  
        return "invalid operator."

print(add(3,3))

name()

for i in range (10):
    print(add(3,8))


namelist = []

while True:
    print("\nAktuell lista:")
    for i, name in enumerate(namelist):
        print(f"{i}: {name}")

    choice = input("Do you want to [A]dd till, [R]emove, [C]hange ett namn eller [E]nd? ").lower()

    if choice == "a":
        name = input("give a name to add: ")
        addnamelist(namelist, name)
    elif choice == "r":
        index = int(input("give the index of the name to be removed: "))
        removenamelist(namelist, index)
    elif choice == "c":
        oldname = input("which name do you want to change?: ")
        newname = input("enter the name: ")
        editnamelist(namelist, oldname, newname)
    elif choice == "e":
        print("endig program.")
        break
    else:
        print("wrong choice.")

        
    
        

num1 = int(input("give a number: "))


operator = input("give a + - * or /: ")

num2 = int(input("give another number:"))

print(calculate(num1, num2, operator))





    




