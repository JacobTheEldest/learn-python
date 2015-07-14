#This program calculates the fibonacci sequence in a simpler way
a = 0
b = 1
count = 0
iterations = int(input("How many numbers do you want generated? "))


while count < iterations:  
    print(a, end=" ")

    count += 1

    if count < iterations:
        print(b, end=" ")
        
    count += 1
    
    a += b
    b += a

print()
