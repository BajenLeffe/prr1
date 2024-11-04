import os
os.system('cls')

for table in range(1, 13):
    print(f"{table}-tabellen")
    for x in range(1, 11):
        print(f" {table} * {x}= {table*x}")