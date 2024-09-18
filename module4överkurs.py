import os
os.system('cls')

while True:
    try:
        base = int(input("give a base: "))
        exponent = int(input("give an exponent: "))
        break
    except:
        print("try again, no letters or floats")
        continue


result = 1


for i in range(exponent): 
    result = result * base 


print(f"{base} to the power of {exponent} is {result}")
print("kontroll svar: ", base**exponent)


