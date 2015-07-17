count = 0
total = 0.0
number = 1

print("Enter 0 to exit the loop")

while number != 0:
    number = float(input("Enter a number: "))
    if number != 0:
        count += 1
        total += number
    if number == 0:
        print("The average was:", total / count)
