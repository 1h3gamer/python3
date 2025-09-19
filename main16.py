print("select your ride")
print("1. BIKE")
print("2. CAR")

choice = int(input("Enter your choice: "))

if (choice == 1):
    print("What type of bike")
    print("1. Scooty\n")
    print("2. Scooter\n")
    choice2 = int(input("Enter your choice2: "))
    if (choice2 == 1):
        print("You have selected a scooty")
    else:
        print("You have selected a scooter")

elif (choice == 2):
    print("What type of car")
    print("Sedan\n")
    print("SUV\n")

    choice3 = int(input("Enter your choice3: "))
    if (choice3 ==1):
        print("You have selected a sedan")
    else:
        print("Yo have selected an SUV")

else:
    print("Wrong choice")