import turtle
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
    #print("Get_X function result (default 250) ",result)
    return result # or return x - MAX_X

def get_y(y):
    '''Converts left coordinate value to cartesian coordinate
    '''    
    result = MAX_Y - y
   #print("Get_Y function result (default 50)",result)
    return result # or return MAX_Y - y

def ltc_goto(x,y):
    '''Left to cartesian goto
    '''
    #print ("LTC function coordinate result (", get_x(x), ", ", get_y(y), "). Woo!", sep="")
    turtle.goto(get_x(x),get_y(y))
                                    # or 
                                    # turtle_x = get_x(x)
                                    # turtle_y = get_y(y)
                                    # turtle.goto(turtle_x, turtle_y)


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

    ltc_goto(50,125)
    draw_rectangle(50, 100, "Blue")

    ltc_goto(300,350)
    draw_rectangle(200, 55, "Red")

    ltc_goto(200,170)
    draw_rectangle(100, 35, "Green")

    ltc_goto(250,125)
    draw_rectangle(75, 75, "Black")


    turtle.done()


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

    turtle.end_fill()
    turtle.penup()
    # End of shape filling or something. Finishes drawing the shape basically

    turtle_position(posx, posy, heading, perimeter) # Pastes the position and perimeter of the shape in addition to the direction that the turtle is facing towards
    return perimeter # We want to return or paste the perimeter value of the current shape

def turtle_position(posx, posy, heading, perimeter):
    '''Prints the values for the varaibles in a pretty fancy,not-so-fancy, but also fancy and legible way
    Also prints perimeter
    '''
    print("The turtle is currently at (", posx, ", ", posy, "), facing or heading towards = ", heading, " degrees.", sep="")
    print("The perimeter of the shape is, ", perimeter, "\n", sep="")


def main():
    init()

   # get_x(250)
   # get_y(50)

if __name__ == "__main__":
    main()