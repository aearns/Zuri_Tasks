# Rock Paper Scissors Game

import random
#from time import puase

options = ["Rock", "Paper", "Scissors"]
user_options = ["R", "r", "s", "S", "P", "p"]

is_running = True

while is_running:
    def welcome():
        print('Welcome to Rock Paper Scissors')
        print("Rock beats Scissors\nPaper beats Rock\nScissors beats Paper")
        print("R is for Rock\nP is for Paper\nS is for Scissors")

welcome()
computer = (random.choice(options))
answer = []
answer.append(computer)
# User makes a selection
input_user = input("Please choose R, P, or S:\n")

# If conditions are met
if (input_user in user_options):
    print("Great choice")
    if input_user == user_options[0] or input_user == user_options[1]:
            print("You have selected", options[0])
    elif input_user == user_options[2] or input_user == user_options[3]:
        print("You have selected", options[2])
    elif input_user == user_options[4] or input_user == user_options[5]:
        print("You have selected", options[1])
else:
    print("Sorry, please select R, P or S")

def new_game():
    if (input_user == answer):
        print ("Oops! It's a draw")
    if (input_user == "Rock" and answer == "Scissors"):
        print ("Congratulations! You won. Rock crashes Scissors")
    elif (input_user == "Rock" and answer == "Paper"):
        print ("Sorry, you lost. Paper wraps Rocks")

    if (input_user == "Scissors" and answer == "Paper"):
        print ("Congratulations! You won. Rock crashes Scissors")
    elif (input_user == "Scissors" and answer == "Rock"):
        print ("Sorry, you lost. Rock crushes Scissors")

    if (input_user == "Paper" and answer == "Rock"):
        print ("Congratulations! You won. Paper wraps Rock")
    elif (input_user == "Paper" and answer == "Scissors"):
        print ("Sorry, you lost. Scissors cuts Paper")
new_game()

# def new_game():
#     if computer == answer:
#         print("Draw")
#     elif game == "R" and answer != "P":
#         print("You win")
#     elif game == "P" and answer != "S":
#         print("You win")
#     elif game == "S" and answer != "R":
#         print("You win")
#     else:
#         print('Sorry you lost')
#     print(f"Computer choose {answer}")
# new_game()

choice = input("Let's play again? Y/N: ")
if choice == "Y":
    pass
if choice == "N":
    is_running = False
print("See you again next time!") 
is_running = False
