# This is Python game
import random
options = ['R', 'P', 'S']

var = ['R', 'P', 'S']
def game(R, P, S):
    Pick1= 'R'
    Pick2= 'P'
    Pick3= 'S'
print (game)

print('Welcome to Rock Paper Scissors')
print('This is a simple game.\nPlayer vs Computer. Choose Rock')
user = str(input('Please select your option R, P or S: '))
for i in range(var):
    print("Let's play!")
if user == game:
    print("Your choice is, ", user)
else:
    print('Invalid options. Please select R, P, or S')
# comp = random.choice(options)

while user == game:
    print("Your choice is,",user)
    comp = random.choice(options)
    if comp == user:
        print('Congratulations, you win')
    else:
        print('Sorry, you lost. Please play again')
else:
    print('Invalid options. Please select R, P, or S')

# for i in game i:
#     print('You have selected', i)
#while user == game:
#    print('You selected', user)
#    print("Now, let's play Rock Paper Scissors")
# else:
#     print('Sorry, please select R, P or S')
#     break;

# if comp == user:
#     print('Congratulations, you win')
# else:
#     print('Sorry, you lost')
#     print('Computer selected:', comp)


#again (input('Would you like to play again? Y/N' ))
#if again == Y:
