''' 
Various mathematical formulas
'''

### Radius of circle and sphere formula and calculates area
def circle():
    ''' Calculates radius of circle_math
    '''
    print("Area of Circle and Volume of Sphere")
    radius = int(input("Enter a radius for the area of a circle and volume of sphere! : "))
    circle_math(radius) # Calculates math for circle and sphere

def circle_math(radius):
    ''' Calculates both math and math_sphere for circle
    '''
    math = 3.14159*(radius**2) # Math for circle
    math_sphere = (4/3)*3.14159*(radius**3)
    print("The area of a circle is ", math, 
    "The volume of a sphere is ", math_sphere, sep="")

### Area of rectangle
def rectangle():
    ''' Asks for width and length then calculates rectangle of width and height
    '''
    print("Area of Rectangle")
    width = int(input("Enter a width: "))
    height = int(input("Enter a height: "))
    rectangle_math(width,height)

def rectangle_math(width, height):
    ''' Calculates area of a rectangle
    '''
    math = width * height
    print("The area of a rectangle is: ", math, sep="")

### Area of square
def square():
    ''' Asks for side length then calculates side^2
    '''
    print("Area of Square")
    side = int(input("Enter a side length for a square: "))
    square_math(side)

def square_math(side):
    ''' Calculates area of a square
    '''
    print("The area is: ", side**2, sep="") # Math for s^2

### Area of iscoceles triangle
def isosceles_triangle():
    ''' Asks for side and height then calculates (sh)/2
    '''
    print("Area of Isosceles Triangle")
    side = int(input("Enter a side: "))
    height = int(input("Enter a height: "))
    isosceles_triangle_math(side,height)

def isosceles_triangle_math(side,height):
    math = (side*height)/2 # Calculates math for (bh)/2
    print("The area is:", math, sep="")

### Area of equilateral triangle
def equilateral_triangle():
    ''' Asks for side then calculates (sqrt(3)/4)(a**2)
    '''
    print("Area of Equilateral Triangle")
    side = int(input("Enter a side: "))
    equilateral_triangle_math(side)

def equilateral_triangle_math(side):
    math = (1.73205/4)*(side**2) # Math for equilateral triangle sqrt(3) ~= (estimates to) 1.73205
    print("The area is: ", math, sep="")

def trapezoid():
    ''' Asks for 3 variables:
    base1 = a
    base2 = b
    height = h
    Formula: h((a+b)/2)
    '''
    print("Area of trapezoid")
    base1 = int(input("Enter a base: "))
    base2 = int(input("Enter another base: "))
    height = int(input("Enter a height: "))
    trapezoid_math(base1, base2, height) # Grabs variables from base1,base2 and height

def trapezoid_math(base1, base2, height):
    math = ((base1*base2)/2)*height # Prints int variables from trapezoid()
    print("The area of a trapezoid is: ", math, sep="") # prints math

### Executes code
def main():
    circle()
    circle()
    rectangle()
    rectangle()
    square()
    square()
    isosceles_triangle()
    isosceles_triangle()
    equilateral_triangle()
    equilateral_triangle()
    trapezoid()
    trapezoid()
main()