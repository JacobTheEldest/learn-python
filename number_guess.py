'''
https://www.reddit.com/r/beginnerprojects/comments/19jj9a/project_higherlower_guessing_game/

MAIN GOAL

-Create a simple game where the computer randomly selects a number between 1
and 100 and the user has to guess what the number is.
-After every guess, the computer should tell the user if the guess is higher or
lower than the answer.
-When the user guesses the correct number, print out a congratulatory message.

SUBGOALS

-Add an introduction message that explains to the user how to play your game.
-In addition to the congratulatory message at the end of the game, also print
out how many guesses were taken before the user arrived at the correct answer.
-At the end of the game, allow the user to decide if they want to play again
(without having to restart the program).

'''

import random

play = 'y'

def random_num(max):
    return random.randint(1, max)

def evaluate_guess(guess, answer):
    guess = int(guess)
    answer = int(answer)
    if guess == answer:
        return True
    elif guess > answer:
        print("{} is too high.".format(guess))
        return False
    elif guess < answer:
        print("{} is too low.".format(guess))
        return False

def setup():
    while True:
        print("\n\nChoose a max number.")
        upper = input()
        if upper.isdigit() and int(upper) > 1:
            return (int(upper), random_num(int(upper)))
            break
        else:
            print("Please pick a number greater than 1.\n\n")

            
#Setup
answer = ''
upper = ''
guesses = 0
guess = 0
setup()


while play.lower() in ['', 'y', 'yes']:
    if evaluate_guess(guess, answer) == True:
        (upper, answer) = setup()
        
    guess = int(input("\nGuess a number between 1 and {}: ".format(upper)))
    guesses += 1

    if evaluate_guess(guess, answer) == True:
        print("{} is correct! It took you {} guesses.".format(guess, guesses))
        print("\nDo you want to play again? [y/n]")
        play = input()
        
