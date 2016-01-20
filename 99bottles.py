'''
https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

GOAL
Create a program that prints out every line to the song "99 bottles of beer on
the wall." This should be a prettysimple program, so to make it a bit harder,
here are some rules to follow.

RULES
-If you are going to use a list for all of the numbers, do not manually type
them all in. Instead, use a built in function.

-Besides the phrase "take one down," you may not type in any numbers/names of
numbers directly into your song lyrics.

-Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

-Put a blank line between each verse of the song.
'''

#Initialize Variable
print("How many bottles of beer on the wall?")
repeat = int(input())

def verse(number):
    '''Print "99 bottles" verse with verse number as an argument'''

    if number > 1:
        print("\n" + str(number) + " bottles of beer on the wall,")
        print(str(number) + " bottles of beer!")
        print("Take one down. Pass it around.")
        print(str(number - 1) + " bottles of beer on the wall.")
    elif number == 1:
        print("\n" + str(number) + " bottle of beer on the wall,")
        print(str(number) + " bottle of beer!")
        print("Take it down. Pass it around.")
        print(str(number - 1) + " bottles of beer on the wall.")
    else:
        print("\n" + "Invalid bottles of beer on the wall.")


for num in range(repeat, 0, -1):
    verse(num)
