import os
os.system('cls')

cpu = [
         {
            "make":"AMD ryzen" ,
            "perfclass": 7,
            "model":"5700X3D",
            "clock": "4.1ghz"
        },
         {
            "make":"AMD ryzen" ,
            "perfclass": 5,
            "model":"5600",
            "clock": "4.4ghz"
        },
         {
            "make":"AMD ryzen", 
            "perfclass": 9,
            "model":"5900XT",
            "clock": "4.8ghz"
        }
]


while True:
    for cpus in cpu:
        make = cpus['make']
        perfclass = cpus['perfclass']
        model = cpus['model']
        clock = cpus['clock']
        print(f"{make} {perfclass} {model} {clock}")

    
    choice = int(input("1 = add, 2 = remove, 3 = edit: "))
    if choice == 1:
        make = input("manufacturer: ")
        perfclass = input("performance class: ")
        model = input("model number: ")
        clock = input("clock speed: ")
        cpu.append(
        {
            "make": make,
            "perfclass": perfclass, 
            "model": model,
            "clock": clock,
        }
    )

    elif choice == 2:
        index = int(input("CPU number to remove: "))    
        if 0 <= index:
            cpu.pop(index)
            print("CPU removed.")
        else:
            print("Invalid number.")
        

    elif choice == 3:
        index = int(input("CPU number to edit: "))   
        old_make = cpu[index]['make'] 
        old_perfclass = cpu[index]['perfclass'] 
        old_model = cpu[index]['model'] 
        old_clock = cpu[index]['clock']

        new_make = input(f"type new manufacturer ({old_make}): ")
        new_perfclass = input(f"type new performance class ({old_perfclass}): ")
        new_model = input(f"type new model ({old_model}): ")
        new_clock = input(f"type new clock speed ({old_clock}): ")
        
        cpu[index]['make'] = new_make
        cpu[index]['perfclass'] = new_perfclass
        cpu[index]['model'] = new_model
        cpu[index]['clock'] = new_clock

        print(f"CPU at index {index} has been updated.")

        



    else:
        print("invalid option!")

   
    

