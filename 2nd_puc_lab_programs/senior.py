name=input("Enter your name: ")
birth_year=int(input("Enter your birth year: "))
current_year=int(input("Enter the current year: "))
if birth_year > current_year:
    print("Invalid input. Birth year cannot be greater than current year.")
else:
    if (current_year-birth_year) >= 18: 
        print("You are eligible to vote.")
    elif(current_year-birth_year) < 18:
        print("you are not eligible to vote.")
    else:
        print("Invalid input.")