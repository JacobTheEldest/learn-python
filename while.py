add = 1
total = 0

print("Enter numbers to add to the total.")
print("Enter 0 to quit.")

while add != 0:
    print("Current Total:", total)
    add = float(input("Number? "))
    total += add

print("Final total =", total)
