# Rock Paper Scissors Game

import random
#from time import puase
options = ["Rock", "Paper", "Scissors"]

is_running = True

while is_running:

    def welcome():
        print('Welcome to Rock Paper Scissors')
        print("R is for Rock\nP is for Scissors\nS is for Scissors" )
    welcome()

    user_input = input("Please select R, P or S: ")

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
    
    print("Computer is making a choice")
  #  wait(0.5)

    # Rock beats Scissors
    # Paper beats Rock
    # Scissors beats Paper

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

    choice = input("Let's play again? Y/N: ")
    if choice == "Y":
        pass
    if choice == "N":
        is_running = False
print("See you again next time!")