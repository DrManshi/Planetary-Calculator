
print("\n*** Hey Fellas! Welcome! ***")
print("Here you can find your age and weight on different planets in our solar system!\n")
print("So, do you want to find out your age or weight on different planets?")
answer = input("Type 'Age' for age calculator or 'Weight' for weight calculator: ").strip().lower()
if answer == "weight":
    print("\nAre you ready to find out how much you would weigh on different planets ?!")
    choice = input("Type 'Yes' to continue or 'no' to exit: ").strip().lower()
    if choice == "no":
        print("Alright, but if you change your mind, this weight calculator will always be here!")
    elif choice == "yes":
        print("\n********Great! Let's get started!********\n")
     
        wRatios = {"MERCURY":0.38, "VENUS":0.91, "EARTH":1.0, "MARS":0.38, "JUPITER":2.34, "SATURN":1.06, "URANUS":0.92, "NEPTUNE":1.19}
        userWeight = float(input("Enter your weight on Earth (in kilograms): "))
        planet = input("Enter the name of the planet you want to calculate your weight on: ").strip().upper()
 
        if planet not in wRatios:
            print("\nAhah! That's not a valid planet name. Please restart the program and enter a valid planet next time!")
        else: 
            weightOnPlanet = float(userWeight)*wRatios[planet]
            print("\n--------Your weight on " + planet + " would be: " + str(weightOnPlanet) + " kilograms--------\n")
            print("Wow! Isn't that interesting?")
            print("Would you like to try another planet?\n")
            another = input("Type 'Yes' to try again or 'No' to exit: ").strip().lower()
            if another == "yes":
               print("\nRestart the program to try again!\n")
            elif another == "no":
               print("\nThanks for using the weight calculator! Have a great day!\n")
            else:
               print("\nInvalid input. Please enter 'Yes' or 'No'.\n")
           
    else:
         print("\nInvalid input. Please enter 'Yes' or 'No'.\n")
elif answer == "age":
    eAge = input("\nEnter your age in years: ")
    pName = input("On which planet do you want to know your age? ").strip().upper()
    ageRatios = {"MERCURY":0.24, "VENUS":0.62, "EARTH":1.0, "MARS":1.88, "JUPITER":11.86, "SATURN":29.46, "URANUS":84.01, "NEPTUNE":164.8}
    if pName not in ageRatios:
        print("\nAhah! That's not a valid planet name. Please restart the program and enter a valid planet next time!")
    else:
        pAge = float(eAge)/ageRatios[pName]
        print("\nYour age on " + pName + " would be: " + str(pAge) + " years.\n")
        print("Wow! Isn't that fascinating?")
        print("Would you like to try another planet?\n")
        anotherAge = input("Type 'Yes' to try again or 'No' to exit: ").strip().lower()
        if anotherAge == "yes":
            print("\nRestart the program to try again!\n")
        elif anotherAge == "no":
            print("\nThanks for using the age calculator! Have a great day!\n")
        else:
            print("\nInvalid input. Please enter 'Yes' or 'No'.\n")
else:
    print("\nInvalid input. Please restart the program and type either 'Age' or 'Weight'.\n")
 
