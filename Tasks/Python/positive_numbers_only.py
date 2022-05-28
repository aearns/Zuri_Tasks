number = input("Enter a number: ")

# Validation
try:
    # Runs if input is valid
    number = float(number)
    print("Excellent, you entered a number")

    if number >= 0:
        print("This is a postive number")
    
    else:
        print("Sorry, not a positive number")

except:
    print("User input is not a number. Please enter a number")  # Runs if input is invalid