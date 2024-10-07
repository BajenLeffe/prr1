import os
os.system('cls')

"""
while True:
    print("="*90)

    print("alla gångertabeller upp till 12")

    counter = 1
    times = int(input("välj din gångertabell: "))

    while counter != 13:
        
        print(f"{counter} * {times} = {counter * times}")
        counter += 1
        """

for table in range(1, 13):
    print(f"{table}-tabellen")
    for x in range(1, 11):
        print(f" {table} * {x}= {table*x}")