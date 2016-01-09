'''
https://www.reddit.com/r/beginnerprojects/comments/19jwi6/project_pythagorean_triples_checker/http://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/

MAIN GOAL

-Imagine that your friend is a cashier, but has a hard time counting back change
to customers. Create a program that allows him to input a certain amount of
change, and then print how how many quarters, dimes, nickels, and pennies are
needed to make up the amount needed.

SUBGOALS

-So your friend doesn't have to calculate how much change is needed, allow him
to type in the amount of money given to him and the price of the item. The
program should then tell him the amount of each coin he needs like usual.

-Loop the program so the user can use it more than once without having to
restart the program.

'''


#Initialize variables
loop = 'y'
cash = 0
cost = 0
change = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0


#Loop as long as user wants.
while loop.lower() in ('y', 'yes', ''):

    cost = float(input("\nCost of item: "))
    cash = float(input("Cash given:   "))

    if cost > cash:
        print("Insufficient funds.")
        continue
    
    change = float('{:.2f}'.format(cash - cost))

    quarters = int(change // .25)
    change = change - (quarters * .25)

    dimes = int(change // .10)
    change = change - (dimes * .10)

    nickels = int(change // .05)
    change = change - (nickels * .05)

    pennies = int(change // .01)

    print("\nChange is {:.2f} distributed as follows:".format(cash - cost))
    print("{} Quarters".format(quarters))
    print("{} Dimes".format(dimes))
    print("{} Nickels".format(nickels))
    print("{} Pennies".format(pennies))

    loop = input("\n{Enter} to continue.\n")
