"""
Test file for Polygon Flower.
You do not need to comment this code except for adding your name.

@author: Jin Moon
"""

import poly_flower as pf
from testing import *
import turtle as t

# Activity 1 Test (See practicum writup for details)
def test_validate_number_valid ():
    #Setup
    pf.init()
    #Invoke
    isvalid_num = pf.validate_number(5)
    #Analyze
    assert_equals("valid input", 5, isvalid_num)

 
# Activity 1 Test (See practicum writup for details)
def test_validate_number_invalid ():
    #Setup
    pf.init()
    #Invoke
    isnotvalid = pf.validate_number("Sup")
    #Analyze    
    assert_none("invalid input", isnotvalid)


# Activity 2 Test (See practicum writup for details)
def test_get_color_green ():
    #Setup
    pf.init()
    #Invoke
    color_green = pf.get_color(7)
    #Analyze    
    assert_equals("get color green", "green", color_green)
    
# Activity 3 Test (See practicum writup for details)
def test_draw_hexagon ():
    #Setup
    pf.init()
    #Invoke
    perimeter = pf.draw_polygon(5,5,"Orange")
    #Analyze
    assert_equals("xcor", 5, round(t.xcor()))
    assert_equals("ycor", 0, round(t.ycor()))
    assert_equals("color", "Orange", t.fillcolor())
    assert_equals("perimeter", 25, perimeter)

# Activity 4 Test (See practicum writup for details)
def test_draw_octogon_circle ():
    #Setup
    pf.init()
    #Invoke
    perimeter = pf.draw_poly_circle(8,50,"Blue")

    #Analyze
    assert_equals("color", "Blue", t.fillcolor())
    assert_equals("perimeter", 400, perimeter)

# Activity 5 Test (See practicum writup for details)
def test_draw_poly_flower ():
    #Setup
    pf.init()
    side_length = 100
    start_sides = 8
    end_sides = 2
    #Invoke
    total_perimeter = pf.draw_poly_flower (side_length, start_sides, end_sides)

    #Analyze
    assert_floats("total perimeter for all flowers", 19000, total_perimeter)

def run_all_tests ():
    run_test(test_validate_number_valid)
    run_test(test_validate_number_invalid)
    run_test(test_get_color_green)
    run_test(test_draw_hexagon)
    run_test(test_draw_octogon_circle)
    run_test(test_draw_poly_flower)
    pass

run_all_tests ()