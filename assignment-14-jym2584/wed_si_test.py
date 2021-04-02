from wed_si import *
import turtle
def rectangle():
    length = 100
    
    triangle(length)

    assert turtle.fillcolor() == "orange"
    assert round(turtle.xcor()) == 0
    assert round(turtle.ycor()) == 0
    assert turtle.isdown() == False
