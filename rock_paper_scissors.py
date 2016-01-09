'''
https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

You must make a rock paper scissors game

Goal

-Ask the player if they pick rock paper or scissors
-Have the computer chose its move
-Compare the choices and decide who wins
-Print the results

Subgoals

-Let the player play again
-Keep a record of the score e.g. (Player: 3 / Computer: 6)GOAL
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty
simple program, so to make it a bit harder, here are some rules
to follow.
'''


#Imports
import time
from random import randint


#Initialize Variables
user = input("What's your name?")
user_score = 0
computer_score = 0
play = 'y'

#Dictionaries to define choices
num_to_name = {0: 'rock', 1: 'paper', 2: 'scissors'}


def random_choice():
    return randint(0,2)

while play.lower() in ('y', 'yes', ''):
    user_choice = int(input('\n0: Rock \n1: Paper \n2: Scissors \n'))

    if user_choice < 0 or user_choice > 2:
        print("Please reconsider your choice.\n")
        continue
    
    computer_choice = random_choice()
    print("\nComputer chooses {}\n".format(num_to_name[computer_choice]))

    comparison = (computer_choice - user_choice) % 3

    if comparison == 1:
        print("Computer wins this round!")
        computer_score += 1
    elif comparison == 2:
        print("You win this round!")
        user_score += 1
    else:
        print("This round is a draw.")

    print("\n{}: {}".format(user, user_score))
    print("\nComputer: {}".format(computer_score))

    play = input("\nPlay again? [y/n]\n")

#Close
print("Thanks for playing!")

if user_score > computer_score:
    print("You won overall with a score of {} to {}.".format(user_score, computer_score))
elif computer_score > user_score:
    print("Computer won overall with a score of {} to {}".format(computer_score, user_score))
else:
    print("Draw with a score of {}".format(user_choice))
