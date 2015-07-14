#This program calculates the fibonacci sequence
a = 0
b = 1
count = 0
iterations = int(input("How many numbers do you want generated? "))

while count < iterations:
    count += 1
    print(a, end=" ")

    old_a = a
    a = b
    b = old_a + b

print()
