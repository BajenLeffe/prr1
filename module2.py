#module 2 - variables
"""
string = "text"
integer = 1... 2... 3... 10...
float = 1.2 

boolean = true/false    flag for on and off
    

deklare/initiate

"""

#initate (name of the variable and data type)
name = "" #string
value = 1.3 #float
value2 = 8 #integer
value3 = 8.1 #float
check = False #boolean

import os
os.system("cls")

print("select random numbers")
x = int(input("x: ")) #input has to be type converted before you make calculations otherwise it will throw it in as a string
y = int(input("y: "))

print(x * y)

print("=" * 90)
print("please input your weight and height")
weight = float(input("weight (in kg): "))
height = float(input("height (in M): "))

bmi = weight / height ** 2

print("your BMI is", bmi)

#the power of is done with ** and division with no decimals is done with //
#modulo is done with % and shows the rest of a division


Kg = weight

weight_in_lbs = Kg * 2.20462262

print("\n", "also your weight in lbs is: ", weight_in_lbs)

print("=" * 90)
current_age = int(input("insert your age: "))

age_in_weeks = current_age * 52.176

print("\n", "your age in weeks is: ", age_in_weeks)

print("=" * 90)

name = input("write name:")
age = current_age

print(f'welcome {name} you are {age} years old and your BMI is {bmi} and you age in weeks is: {age_in_weeks} also your weight in lbs is {weight_in_lbs}')







