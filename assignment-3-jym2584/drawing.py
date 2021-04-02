import turtle
import math
''' This file draws some cool stuff. Like a square so far! 
Also prints position, degree and perimeter of the shapes

Copy from drawing.py (Mon, Aug 31 assignment) for Wed, Sep 2
Jin Moon
'''

# Global Variables
MAX_X = 200 
MAX_Y = 200
MIN_X = -MAX_X
MIN_Y = -MAX_Y
SPEED = 5

def get_x(x):
    '''Converts left coordinate value to cartesian coordinate
    '''
    result = x + MIN_X
    #print(x)
    #print("Get_X function result (default 250) ",result)
    if x >= 0 and x <= MAX_X - MIN_X:
        #print(x)
        #print(result)
        return result # or return MAX_Y - y
    else: 
        return None

def get_y(y):
    '''Converts left coordinate value to cartesian coordinate
    '''    
    # y >= 0 and y <= MAX_Y - MIN_Y then return result, otherwise return None
    result = MAX_Y - y
    if y >= 0 and y <= MAX_Y - MIN_Y:
        return result # or return MAX_Y - y
    else: 
        return None

def ltc_goto(x,y):
    '''Left to cartesian goto
    '''
    #print ("LTC function coordinate result (", get_x(x), ", ", get_y(y), "). Woo!", sep="")
    #turtle.goto(get_x(x),get_y(y))
                                    # or 
    turtle_x = get_x(x)
    turtle_y = get_y(y)
    if turtle_x != None and turtle_y != None:
        turtle.goto(turtle_x, turtle_y)
    else:
        print("(", x, ", ", y, ") is not a valid coordinate", sep="")


def init():
    ''' Draws a squared border so far (screen dimensions)
    '''
    # This sets up the border before drawing it
    turtle.speed(0)
    turtle.penup()
    turtle.forward(MIN_X)
    turtle.left(90)
    turtle.forward(MAX_Y)
    turtle.right(90)

    draw_border(MAX_X*2) # Draws the border
                         # or
                         # draw_rectangle(MAX_X*2, MAX_Y*2, "")
                         # Didn't really have to make another border function


def draw_border(length):
    '''Creates a border
    '''
        # This creates the 4 sided shape
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(length)
    
    turtle.right(90)
    turtle.forward(length)
    
    turtle.right(90)
    turtle.forward(length)

    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.penup()


def draw_rectangle(lengthx, lengthy, color):
    '''Creates a square with specified variables
    lengthx = object length
    lengthy = object width
    color = fill-in color of the object
    '''

    # Variables
    posx  = turtle.xcor()
    posy = turtle.ycor()
    heading = turtle.heading()
    turtle.speed(SPEED)
    perimeter = 0 # We want to calculate the perimeter of the individual shapes

    # This creates the 4 sided shape
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(lengthx)
    perimeter = perimeter + lengthx # Perimeter becomes 0 + length
    
    turtle.right(90)
    turtle.forward(lengthy)
    perimeter = perimeter + lengthy # Perimeter becomes length + length yada yada
    
    turtle.right(90)
    turtle.forward(lengthx)
    perimeter = perimeter + lengthx

    turtle.right(90)
    turtle.forward(lengthy)
    perimeter = perimeter + lengthy
    
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    # End of shape filling or something. Finishes drawing the shape basically

    turtle_position(posx, posy, heading, perimeter) # Pastes the position and perimeter of the shape in addition to the direction that the turtle is facing towards
    return perimeter # We want to return or paste the perimeter value of the current shape


def turtle_position(posx, posy, heading, perimeter, shape):
    '''Prints the values for the varaibles in a pretty fancy,not-so-fancy, but also fancy and legible way
    Also prints perimeter
    '''
    print("DRAWING:", shape)
    print("The turtle is currently at (", posx, ", ", posy, "), facing or heading towards = ", heading, " degrees.", sep="")
    print("The size of the ", shape, " is, ", perimeter, "\n", sep="")


def get_color (color_code):
    '''Gets the initial of the color and translates it into text
    '''
    if color_code == "r":
        return "red"
    elif color_code == "o":
        return "orange"
    elif color_code == "g":
        return "green"
    elif color_code == "b":
        return "blue"
    elif color_code == "p":
        return "purple"
    else:
        return ""

def rectangle_will_fit(x,y,length,height):
    '''Check if the rectangle will fit
    '''
    endlength = x + length
    endheight = y + height

    if x < 0 or x > MAX_X*2 or y < 0 or y > MAX_Y*2:
        return 0 # returns false if coordinates are less than 0 or greater than 400, same with y
    elif endlength < 0 or endlength > MAX_X*2 or endheight < 0 or endheight > MAX_Y*2:
        return 0 # returns false if coordinates + shapes are less than 0 or greater than 400
    else:
        return 1 # returns true if the 2 conditions are met within bounds



    """
    turtle.xcor()
    if turtle.xcor() < 0 or turtle.ycor() < 0:
        return None, "Out of bounds 1"
    elif (get_x(x) + length) > MAX_X or (get_y(x) + length) > MAX_Y:
        return None, "Out of bounds 2"
    else:
        print("The shape fits")
    """

def translate_shape_initial(initial):
    '''Gets the initial of the shape and translates it into text
    '''
    if initial == "r":
        return "rectangle"
    elif initial == "t":
        return "triangle"
    elif initial == "c":
        return "circle"
    else:
        pass
def draw_shape(shape,color,x,y,length,height = 0):
    '''Draws the shape
    '''
    # Variables
    posx  = round(turtle.xcor(),0)
    posy = round(turtle.ycor(),0)
    heading = turtle.heading()
    turtle.speed(SPEED)

    ltc_goto(x,y)
    translatecolor = get_color(color) # get color initial r == Red
    translatedshape = translate_shape_initial(shape) # get shape initial r == rectangle
    if (rectangle_will_fit(x,y,length,height) == 0): # If the shape does not fit then
        '''Print the statement that the shape is out of bounds with variables:
        x, y, length and height
        '''
        print ("Your shape, ", translatedshape, " is out of bounds! (CURRENT BOUNDARIES: ", MAX_X*2, ", ", MAX_Y*2, ") Check your x or y (",x,",",y, ") and length or width (",length,", ", height, ") values to resolve the error.\n  ERROR: x + length = ", x + length, " and y + height = ", y + height, "\n", sep="")
    else: # If the shape does fit then we go through identifying the shape
        if translatedshape == "rectangle": #If the shape is a rectangle then 
            perimeter = 0 # We want to calculate the perimeter of the individual shapes
            # This creates the 4 sided shape
            turtle.pendown()
            turtle.fillcolor(translatecolor)
            turtle.begin_fill()
            turtle.forward(length)
            perimeter = perimeter + length # Perimeter becomes 0 + length

            turtle.right(90)
            turtle.forward(height)
            perimeter = perimeter + height # Perimeter becomes length + length yada yada

            turtle.right(90)
            turtle.forward(length)
            perimeter = perimeter + length

            turtle.right(90)
            turtle.forward(height)
            perimeter = perimeter + height

            turtle.end_fill()
            turtle.penup()
            turtle.right(90)
            turtle_position(posx,posy,heading,perimeter, translatedshape) # We want to print the x,y, direction, perimeter and the value of the shape from our draw_rectangle!
            return perimeter
            # End of shape filling or something. Finishes drawing the shape basically
        elif translatedshape == "circle":
            circumference = round((2*math.pi*length),2)
            turtle.pendown()
            turtle.fillcolor(translatecolor)
            turtle.begin_fill()
            
            turtle.circle(50)

            turtle.end_fill()
            turtle.penup()
           # print(circumference)
            turtle_position(posx,posy,heading, circumference, translatedshape)
            return circumference
        elif translatedshape == "triangle":
            perimeter = 0

            turtle.pendown()
            turtle.fillcolor(translatecolor)
            turtle.begin_fill()
            turtle.forward(length)
            perimeter = perimeter + length # Perimeter becomes 0 + length

            turtle.left(120)
            turtle.forward(length)
            perimeter = perimeter + length # Perimeter becomes length + length yada yada

            turtle.left(120)
            turtle.forward(length)
            perimeter = perimeter + length
            turtle.left(120)

            turtle.end_fill()
            turtle.penup()
            turtle_position(posx,posy,heading,perimeter, translatedshape)
            return perimeter
        else: # if the shape is not either a rectangle, circle or circle, then it will not be a valid shape
            print(shape, "is not a valid shape\n")




def main():
   #get_x(0)
    #get_y(400)

    init()
    draw_shape("r", "o", 0, 0, 100, 100)
    draw_shape("r", "r", 300, 200, 200, 200) # Test if the rectangle is out of bounds
    draw_shape("notavalidshape", "r", 200, 200, 200, 200) # Test if the shape is not valid
    draw_shape("c", "r", 100, 320, 20)
    draw_shape("t", "p", 200, 200, 120)
    turtle.done()

if __name__ == "__main__":
   main()