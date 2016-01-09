'''
https://www.reddit.com/r/beginnerprojects/comments/19jwi6/project_pythagorean_triples_checker/

MAIN GOAL

-Create a program that allows the user to input the sides of any triangle, and
then return whether the triangle is a Pythagorean Triple or not.

SUBGOALS

-If your program requires users to input the sides in a specific order, change
the coding so the user can type in the sides in any order. Remember, the
hypotenuse (c) is always the longest side.

-Loop the program so the user can use it more than once without having to
restart the program.

'''


#Initialize variables
loop = 'y'
a = 0
b = 0
c = 0


#Allow user to check another set of numbers
while loop.lower() in ('y', 'yes', ''):

    print("\nPlease enter the three integer sides of your triangle.")
    a = int(input())
    b = int(input())
    c = int(input())

    if a >= b and a >= c:
        a, c = c, a
    elif b >= a and b >= c:
        b, c = c, b

    if (a**2 + b**2) == c**2:
        print("Your values are a pythagorean triple.")
    else:
        print("Your values are not a pythagorean triple.")

    loop = input("\nWould you like to check another set? [y/n]\n")
