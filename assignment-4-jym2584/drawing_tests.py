'''Drawings.py test
'''
import turtle as t
import pixart as p
import drawings as d
from testing import *

def test_draw_pixel_color():
    result = d.draw_pixel_color("0")
    assert_equals("Black color","Black", t.fillcolor())
    resultwhite = d.draw_pixel_color("1")
    assert_equals("color","White", t.fillcolor())
    resultred = d.draw_pixel_color("2")
    assert_equals(" color","Red", t.fillcolor())
    resultyellow = d.draw_pixel_color("3")
    assert_equals(" color","Yellow", t.fillcolor())
    resultorange = d.draw_pixel_color("4")
    assert_equals(" color","Orange", t.fillcolor())
    resultgreen = d.draw_pixel_color("5")
    assert_equals(" color","Green", t.fillcolor())
    resultyellowgreen = d.draw_pixel_color("6")
    assert_equals(" color","Yellowgreen", t.fillcolor())
    resultsienna = d.draw_pixel_color("7")
    assert_equals(" color","Sienna", t.fillcolor())
    resulttan = d.draw_pixel_color("8")
    assert_equals(" color","Tan", t.fillcolor())
    resultgray = d.draw_pixel_color("9")
    assert_equals(" color","Gray", t.fillcolor())
    resultdarkgray = d.draw_pixel_color("A")
    assert_equals(" color","Darkgray", t.fillcolor())

def run_all_tests():
    t.tracer(0)
    run_test(test_draw_pixel_color)


run_all_tests()