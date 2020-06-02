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


def request_guess(lower, upper):
    while True:
        guess = input("\nGuess a number between {} and {}: ".format(lower, upper))
        if guess.isdigit():
            guess = int(guess)
            if (lower <= guess <= upper):
                return guess

def setup():
    lower = upper = ''
    while not lower.isdigit():
        lower = input("\nChoose a positive minimum whole number: ")
        if int(lower) < 1:
            lower = ''
    lower = int(lower)
    while not upper.isdigit():
        upper = input("\nChoose a maximum whole number higher than {}: ".format(lower))
        if int(upper) <= lower:
            upper = ''
    upper = int(upper)
    return (lower, upper, random.randint(lower, upper))


# Game Loop
play = 'y'
while play.lower() in ['', 'y', 'yes']:
    # Reset values
    print("\nInitializing...")
    guess = ''
    guesses = 0
    (lower, upper, answer) = setup()

    # Guess Loop
    while guess != answer:
        guess = request_guess(lower, upper)
        guesses += 1

        if guess == answer:
            print("{} is correct! It took you {} guesses.".format(guess, guesses))
            print("\nDo you want to play again? [Y/n]")
            play = input()
        elif guess > answer:
            print("{} is too high.".format(guess))
            upper = guess - 1
        elif guess < answer:
            print("{} is too low.".format(guess))
            lower = guess + 1
