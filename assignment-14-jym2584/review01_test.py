from review01 import *
import turtle as t

def test_distance():
    #setup
    x = 1
    y = 1
    xx = 4
    yy = 5
    #invoke
    value = distance(x, y, xx, yy)
    #assert
    assert value == 7

def test_triangle():
    x1 = 0
    x2 = 0
    x3 = 4
    y1 = 0
    y2 = 3
    y3 = 0
    perimeter = 12
    color = 'blue'
    speed = 5


    value = triangle(x1, y1, x2, y2, x3, y3)
    assert t.xcor() == x1
    assert t.ycor() == y1 
    assert t.speed() == speed
    assert t.isdown() == False
    assert t.fillcolor() == color
    #assert value == perimeter