# Rock Paper Scissors

import random
options = ["R", "P", "S"]

def welcome():
    print('Welcome to Rock Paper Scissors')
    print("R is for Rock\nP is for Scissors\nS is for Scissors" )
welcome()

user_input = input("Please select R, P or S: ")
# def user():
#     input("Please select R, S or P: ")
# user()

def game():
    if user_input == "R":
        print("You have selected: ", user_input)
    elif user_input == "S":
        print("You have selected: ", user_input)
    elif user_input == "P":
        print("You have selected: ", user_input)
    else:
        print("Sorry, please select R, P or S")
game()

computer = str(random.choice(options))
answer = []
answer.append(computer)

# Rock wins Scissors
# Paper wins Rock
# Scissors wins Paper

def new_game():
    if computer == answer:
        print("Draw")
    elif game == "R" and answer != "P":
        print("You win")
    elif game == "P" and answer != "S":
        print("You win")
    elif game == "S" and answer != "R":
        print("You win")
    else:
        print('Sorry you lost')
    print(f"Computer choose {answer}")
new_game()

new_game1 = input("Let's play again? Y/N: ")
if new_game1 == "Y":
    welcome()
    while new_game1 == "Y":
        new_game()
else:
    print("See you next time!")