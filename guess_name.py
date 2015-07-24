guess = None
count = 0
while guess != "Jacob" and count < 3:
    count += 1
    guess = input("Guess my name: ")
    if guess == "Jacob":
        print("Correct!")
    else:
        print("Nope.")
