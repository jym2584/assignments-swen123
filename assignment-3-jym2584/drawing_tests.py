import drawing
import turtle
import math

def test_get_x(value, expected, id):
    '''Testing get_x value
    '''
    x = drawing.get_x (value)
    assert(x == expected)
    print("Test Get X,", id, "Passed")

def test_get_y(value, expected, id):
    '''Testing get_y value
    '''
    y = drawing.get_y (value) # Getting y value from drawing.py
    assert(y == expected) # If y value matches up with the value that we expect get_y to print out
    print("Test Get Y,", id, "Passed")

def test_goto(valuex, valuey, expectedx, expectedy, id):
    #turtle.tracer(0)
    drawing.ltc_goto(valuex, valuey)
    assert (expectedx == turtle.xcor())
    assert (expectedy == turtle.ycor())
    print("Test turtle goto", id, "Passed")

def test_goto_invalid(valuex, valuey, expectedx, expectedy, id):
    turtle.home()
    drawing.ltc_goto(valuex,valuey)
    assert (valuex != expectedx)
    assert (valuey != expectedy)
    print ("Test turtle goto invalid", id, "Failed")
'''
def test_draw_rectangle():
    a) ltc_goto 50, 125 --> expected can be -150, 75. Could utilize turtle.xcor ycor in some way...
    b) turtle_position has heading, heading can be 0
    c) color from draw_rectangle, expected color can be blue
    d) print perimeter, expected perimeter can be 300

    a) Use xcor and ltc_goto
    b) Keep track of side length
    
    print(drawing.turtle_position(posx,posy,heading, perimeter))
    x = drawing.get_x(turtle.xcor())
    y = drawing.get_y(turtle.ycor())
   # assert(col == expectedcol)
   # assert(dir == expecteddir)
   # assert(per == expectedpir)
'''

def test_draw_rectangle(color, heading, expectedposx, expectedposy):
    tcolor= turtle.fillcolor()
    theading = turtle.heading()
    #per = perimeter = drawing.draw_rectangle()
    #print (per)
    print(theading)
    assert(tcolor == color)
    assert(theading == heading)
    #print (round(turtle.xcor()))
   # print (round(turtle.ycor()))
    assert (expectedposx == round(turtle.xcor()))
    assert (expectedposy == round(turtle.xcor()))
    return None, print("Test_draw_rectangle returned true! Input:", color, ". expected: ", tcolor, sep="")

def test_get_x_invalid(value):
    x = drawing.get_x(value)
    assert (x <= 400), "Out of bounds" # 200 MAX_X
    assert (x >=-200), "Out of bounds 2" #0 MIN_
    return None, print("test_get_x_invalid returned true!")


''' Tests from online lecture'''
def lecture_test_goto():
    '''Step 1
    '''
    drawing.ltc_goto(100,100)
    x = turtle.xcor()
    y = turtle.ycor()
    assert( x == -100)
    assert( y == 100)

def lecture_test_draw_rectangle():
    perimeter = drawing.draw_rectangle(100,50,"Orange")
    assert(perimeter == 300)
    assert(turtle.fillcolor() == "Orange")
    print("Lecture draw rectangle test passed")

def test_get_y_invalid():
    y = drawing.get_y(-1)
    assert (y== None)
    print("Test Get Y Invalid Passed")

def lecture_test_goto_invalid():
    x_init = turtle.xcor()
    y_init = turtle.ycor()
    drawing.ltc_goto(-1,-1)
    x = turtle.xcor()
    y = turtle.ycor()
    assert(x == x_init)
    assert(y == y_init)
    print("Test goto invalid passed")

def lecture_test_goto_invalid_x():
    x_init = turtle.xcor()
    drawing.ltc_goto(10,-1)
    x = turtle.xcor()
    assert(x == x_init)
    print("Test goto invalid X passed")

# Color Tests
def test_get_color(value,expected,id):
    '''Tests if the initial will match the actual word
        r = red
        p = purple
    '''
    color = drawing.get_color(value)
    assert (color == expected)
    print("Test get color", id, "passed")

def test_rectangle_will_fit(x, y, length, height):
    ''' Tests if the rectangle will fit inside of the border
    '''
    result = drawing.rectangle_will_fit(x,y,length,height)
    print(result)
    assert (result != 0)
    print("Rectangle with starting coordinate of X: ", x," Y: ", y, " with Length: ", length, " Height: ", height, " fits within 400x400", sep="")

    """
    turtle.tracer(0)
    #drawing.ltc_goto(-1,-1)
    drawing.ltc_goto(x,y)

    value1= drawing.get_x(x)
    value2= drawing.get_y(y)
    print("Default X and Y will return")
    print(x)
    print(y)
    print("Get_X and Get_Y will return")
    print(value1)
    print(value2)

    drawing.draw_rectangle(length,width,"red")
    assert (x + length < )
    assert (y + width < )
    print("The rectangle is out of bounds (Test triangle will fit invalid)")
    print("Values, x=",(x + length), "y=", (y+width))
    """

def test_draw_shape_rectangle():
    ''' Tests if the rectangle will draw correctly as intended
    '''
    turtle.tracer(0)
    perimeter = drawing.draw_shape("r", "o", 0, 0, 200, 200)
    heading = turtle.heading()
    assert (drawing.get_color("o") == "orange")
    assert (round(turtle.xcor(),0) == -200)
    assert (round(turtle.ycor(),0) == 200)
    assert (perimeter == 800)
    assert (heading == 0)
    print("Rectangle will pass")

    """
    print("\n\n\nTEST_DRAW_SHAPE_RECTANGLE:")
    heading = turtle.heading()
    perimeter = drawing.draw_shape("r","orange",300, 300, 100, 50)
    color = turtle.fillcolor()
    x = round(turtle.xcor(),0)
    y = round(turtle.ycor(),0)
    print(heading)
    print(perimeter)
    print("x coord:", x)
    print("y coord:", y)
    assert (color == "orange")
    assert (x == 100)
    assert (y == -100)
    assert (perimeter == 300)
    assert (heading == 0)
    print("Draw shape test passed\n\n\n")
    """

def test_draw_shape_circle():
    ''' Tests if the circle will draw correctly as intended
    '''
    turtle.tracer(0)
    circumference = drawing.draw_shape("c", "r", 100, 320, 20)
    heading = turtle.heading()
    assert (drawing.get_color("r") == "red")
    assert (round(turtle.xcor(),0) == drawing.get_x(100))
    assert (round(turtle.ycor(),0) == drawing.get_y(320))
    assert (circumference == 125.66)
    assert (heading == 0)
    print("Circle will pass")

def test_draw_shape_triangle():
    ''' Tests if the triangle will draw correctly as intended
    '''
    turtle.tracer(0)
    perimeter = drawing.draw_shape("t", "p", 200, 200, 200)
    heading = turtle.heading()
    assert (drawing.get_color("p") == "purple")
    assert (round(turtle.xcor(),0) == drawing.get_x(200))
    assert (round(turtle.ycor(),0) == drawing.get_y(200))
    assert (perimeter == 600)
    assert (heading == 0)
    print("Triangle will pass")

def test_get_shape(value, expected, id):
    ''' Tests if the shape initial will match the actual word
        r should match up with rectangle
        c = circle
        etc.
    '''
    shapeinitial = drawing.translate_shape_initial(value) # Let's get the value of the initial and translate it into the actual word onto our shapeinitial variable
    assert (shapeinitial == expected) #if the translated word on translate_shape_initial is the same as we expect the function to print out
    print("Shape will pass")

def run_all_tests():
    
    test_draw_shape_rectangle()
    test_draw_shape_circle()
    test_get_shape("r", "rectangle", "RECTANGLE INITIAL")
    test_draw_shape_triangle()
    test_rectangle_will_fit(50,100,150,200)

    #test_rectangle_will_fit(2050,100,150,200)
    #test_get_color("r", "red", "Red")
   # test_get_color("o", "orange", "Orange")
    
    # Lecture Step 1
   # test_get_y(0, drawing.MAX_Y, 3)
    #test_get_y(drawing.MAX_X - drawing.MIN_X, drawing.MIN_Y, 4)

    # Lecture Step 2
   # lecture_test_goto()

    # Lecture Step 3

    # Lecture Step 4
   # lecture_test_draw_rectangle()


    #test_get_y_invalid()
    #lecture_test_goto_invalid()
  #  lecture_test_goto_invalid_x()

    #Step 4
    '''Commented out b/c of the step not working due to lecture
    '''
    #turtle.goto(0,0)
    #drawing.draw_rectangle(50, 100, "Blue")
    #test_draw_rectangle("Blue", 90,0,0)
    #test_get_x (0, -200, 1)
    #test_get_x(400,200, 2)


    ######### Step 1
    ''' Commeted out b/c of the step not working due to lecture
    '''
   # test_get_y(300,-100, 1)
    #test_get_y(500,-300, 2)
    
    
    ######### Step 2
    #test_goto(0,0,-200,200,1)
    #test_goto(drawing.MAX_X*2,drawing.MAX_Y*2,200,-200,2)
    #test_goto(100,200,-100,0,3)

    ######### Step 3
    #test_goto_invalid(0,0,100,100,1)

    ######### Step 5
    #test_get_x_invalid(300)



run_all_tests()