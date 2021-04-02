import turtle
import math

MAX_X = 200
MAX_Y = 200
MIN_X = -MAX_X
MIN_Y = -MAX_Y

def init():
    turtle.speed(3)
    turtle.penup()
    turtle.forward(MIN_X)
    turtle.left(90)
    turtle.forward(MAX_Y)
    turtle.right(90)

    square(MAX_X * 2, "")

def square_properties():
    turtle.speed(5)

def square(length, color):
    perimeter = 0
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(length)
    perimeter = perimeter + length
    turtle.right(90)
    turtle.forward(length)
    perimeter = perimeter + length
    turtle.right(90)
    turtle.forward(length)
    perimeter = perimeter + length
    turtle.right(90)
    turtle.forward(length)
    perimeter = perimeter + length
    turtle.end_fill()
    turtle.penup()
    return perimeter

def main():
    init()
    square_properties()

    turtle.goto(0,0)
    perimeter = square(200, "Blue")
    turtle.goto(200,50)
    square(50, "Red")
    turtle.goto(150,-120)
    square(20,"Blue")

    print("Length = 10, Perimeter =", perimeter)
    x  = turtle.xcor()
    y = turtle.ycor()
    heading = turtle.heading()
    print("Turtle is at", x, ", ", y, "0 heading = ", heading, "degrees.", sep="")

    turtle.done()

main()