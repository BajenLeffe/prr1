import os


my_numbers = [1, 2, 3, 4, 5, 6 ,7]

for number in my_numbers:
    print(number)


names = ["malek", "korkis", "fagerberg"]
names.append("hojanna")


while True:
    os.system('cls')

    for name in names:
        print(name)

    new_name = input("\nadd name?: ")

    names.append(new_name)

    for name in names:
        print(name)

    print("\nwant to remove?")

    delete = input("\nwhich one?: ")
    if delete:
        names.pop(int(delete))
