"""
Main program which is used to draw a polygon based flower.
You do not need to comment this code except for adding your name.

@author: Jin Moon
"""

import turtle as t

"""
Color constants for mapping to integers. Map # to COLOR_#
"""
COLOR_LESS_THAN_3 = "white"
COLOR_3 = "maroon"
COLOR_4 = "red"
COLOR_5 = "orange"
COLOR_6 = "yellow"
COLOR_7 = "green"
COLOR_8 = "blue"
COLOR_9 = "indigo" 
COLOR_10 = "violet"
COLOR_MORE_THAN_10 = "black"

def init (tracer_on = True):
    """
    Initialization function that sets some common
    turtle values.
    @param tracer_on: True to turn the tracer on, False to disable it
    """
    t.reset ()
    t.speed (0)
    t.tracer (tracer_on)

def show ():
    """
    Helper function to enable the tracer.
    """
    t.tracer (True)

# Activity 1 (See practicum writup for details)
def validate_number (num_str):
    num_str = str(num_str)
    if num_str.isdigit() == True:
        num_str = int(num_str)
        #print(num_str, "is a digit")
        return num_str
    else:
        #print(num_str, "is not a digit")
        return None

# Activity 2 (See practicum writup for details)
def get_color (code):
    code = int(code)
    if code < 3:
        return COLOR_LESS_THAN_3
    elif code > 10:
        return COLOR_MORE_THAN_10
    elif code == 3:
        return COLOR_3
    elif code == 4:
        return COLOR_4
    elif code == 5:
        return COLOR_5
    elif code == 6:
        return COLOR_6
    elif code == 7:
        return COLOR_7
    elif code == 8:
        return COLOR_8
    elif code == 9:
        return COLOR_9
    elif code == 10:
        return COLOR_10
    else:
        print("Error")

# Activity 3 (See practicum writup for details)

def draw_polygon (num_sides, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    i = 0
    perimeter = length * num_sides
    while i < num_sides:
        t.forward(length)
        t.right(360/num_sides)
        i+=1

    t.penup()
    t.end_fill()
    #t.forward(length)
    #print("The perimeter for func draw_polygon is", perimeter)
    return perimeter



# Activity 4 (See practicum writup for details)
def draw_poly_circle (num_sides, length, color):
    for i in range(0,num_sides):
        perimeter = draw_polygon(num_sides,length,color)
        t.forward(length/2)
        t.left(360/num_sides)
        poly_perimeter = perimeter * num_sides
    #print("The perimeter for func draw_poly_circle is", poly_perimeter)
    return poly_perimeter

# Activity 5 (See practicum writup for details)
def draw_poly_flower (side_length, start_sides, end_sides):
    total_perimeter = 0
    end_sides = end_sides + 1
    #print(end_sides)
    for i in range(0, start_sides):
        polygon_color = get_color(start_sides)
        poly_perimeter = draw_poly_circle(start_sides, side_length, polygon_color)
        if start_sides > end_sides:
            start_sides -= 1
        else:
            break
        total_perimeter = total_perimeter + poly_perimeter
    #print("The perimeter for func draw_poly_flower is", total_perimeter)
    return total_perimeter

def main ():
    init ()
    
    #draw_polygon(5,10,"orange")
    #draw_poly_circle(5,20,"blue")
    #draw_poly_flower(100,10,2)
    
    # Activity 6 (See practicum writup for details)
    quit = False

    while quit == False: 
        length = input("Whats the length? ")
        start_sides = input("Whats your start size? ")
        end_sides = input("whats your end size? ")

        if validate_number(length) and validate_number(start_sides) and validate_number(end_sides):
            length = int(length)
            start_sides = int(start_sides)
            end_sides = int(end_sides)
            total_perimeter = draw_poly_flower(length, start_sides, end_sides)
            print ("The perimeter for the entire flower is", total_perimeter)
            quit = True
        else:
            print("One or more of the values are not valid!\n")

    t.done ()

if __name__ == "__main__":
    main ()