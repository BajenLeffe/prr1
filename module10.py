import time
import os
from datetime import datetime

while True:
    print("Module 10 date&time")
    print("1. Show today's date and time")
    print("2. Show different time formats")
    print("3. Start clock that updates")
    print("4. Stopwatch")
    print("5. End")
    choice = input("Choose your poison (1-5): ")

    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == "1":
        now = datetime.now()
        print("Current date and time:", now)

    elif choice == "2":
        nu = datetime.now()
        print("Different formats:")
        print("1. YYYY-MM-DD:", nu.strftime("%Y-%m-%d"))
        print("2. HH:MM:SS:", nu.strftime("%H:%M:%S"))
        print("3. Full format:", nu.strftime("%Y-%m-%d %H:%M:%S"))
        print("4. Weekday:", nu.strftime("%A"))
        print("5. Short date:", nu.strftime("%d/%m/%Y"))
        print("\n ")

    elif choice == "3":
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                nu = datetime.now()
                print("Press Ctrl + C to end.")
                print("Current time:", nu.strftime("%H:%M:%S"))
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nclock ended.")

    elif choice == "4":
        input("Press enter to start the stopwatch...")
        start = time.time()
        input("Press enter to stop the stopwatch...")
        slut = time.time()
        sekunder = slut - start
        print(f"The stopwatch ended at {sekunder:.2f} seconds.")

    elif choice == "5":
        print("Ending.")
        break

    else:
        print("Incorrect choice, try again.")
