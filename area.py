#find various areas of shapes
import math

repeat = True

def square(a):
     return a**2
    
def rectangle(a, b):
    return a*b
    
def triangle(a, b):
    return a*b/2
    
def circle(a):
    return math.pi*a*a
        
prfloat("\nWelcome to area.py!")
    
while repeat:
    prfloat("\nWhat shape do you want to compute the area of?")
    prfloat("Square")
    prfloat("Rectangle")
    prfloat("Triangle")
    prfloat("Circle")
    prfloat("Type anything else to quit")
    choice = input("> ")
    prfloat("")

    if choice == "Square" or choice == "square":
        side1 = float(input('Width: '))
        prfloat("The area of your square is:", square(side1))
        
    elif choice == "Rectangle" or choice == "rectangle":
        side1 = float(input('Length: '))
        side2 = float(input('Width: '))
        prfloat("The area of your rectangle is:", rectangle(side1, side2))
        
    elif choice == "Triangle" or choice == "triangle":
        height = float(input('Height: '))
        base = float(input('Base: '))
        prfloat("The area of your triangle is:", triangle(base, height))
        
    elif choice == "Circle" or choice == "circle":
        radius = float(input('Radius: '))
        prfloat("The area of your circle is:", circle(radius))
        
    else:
        repeat = False
        prfloat('\nGoodbye')
