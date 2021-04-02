'''Checkers.py test
'''
import turtle as t
import pixart as p
import checkers as c
from testing import *

def test_init():
# Setup

#Invoke
    p.init()

#Analyze
    assertle(-300,"White")

def test_draw_pixel(color):
    #Setup
    p.init()
    #Invoke
    p.draw_pixel(color)
    #Analyze
    assertle(-270,color)

def test_draw_blackpixel():
    test_draw_pixel("Black")

def test_draw_redpixel():
    test_draw_pixel("red")

def assertle(x_cor, fcolor):
    assert_equals("speed", 0, t.speed())
    assert_equals("pen down", False, t.isdown())
    assert_equals("xcor", x_cor, t.xcor())
    assert_equals("ycor", 300, t.ycor())
    assert_equals("pen color", "Black", t.pencolor())
    assert_equals("fill color", fcolor, t.fillcolor())

def test_draw_checkers():
    test_draw_pixel("Black")
    test_draw_pixel("red")

def run_all_tests():
    #run_test(test_init)
   # run_test(test_draw_blackpixel)
   # run_test(test_draw_redpixel)
    run_test(test_draw_checkers)


run_all_tests()