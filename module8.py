import os
os.system('cls')

def add(x, y):
    return x + y

def name():
    fname = input("First name: ")
    lname = input("Last name: ")
    print(f"Your name is {fname} {lname}")

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
        return "Invalid operator."

print(add(3,3))

name()

for i in range (10):
    print(add(3,8))


num1 = input("give a number: ")

operator = input("give a + - * or /: ")
    
num2 = input("give another number:")

print(calculate())




    




