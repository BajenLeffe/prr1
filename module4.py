import os
os.system('cls')

print("=" * 90)

while True:
    print("haha")
    choice = input("stop? press Q").upper()
    if choice == "Q":
        print('yay!')
        break


count = 0 

while count < 10:
    count += 1
    print(str(count) + ") list item")

print("=" * 90)
    

for i in range(10):
    print(i)

print("=" * 90)



name = "your mom"

for letter in name:
    print(letter)

print("=" * 90)

    
numbers = [2,4,6,7,3,7,8]

print(numbers)

for number in numbers:
    print(number)

print("=" * 90)

for table in range(1, 13):
    for x in range(1, 11):
        print(f" {table} * {x}= {table*x}")



