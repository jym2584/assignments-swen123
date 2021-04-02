import turtle as t
import pixart as p
import shape_art as s
import pixart_test as pt
from testing import *

def test_shape_art():
    #setup
    #invoke
    s.shape_art("s 5 5 4 red")
    #analyze
    pt.assertle(t.xcor(), t.ycor(), t.fillcolor())

def run_all_rests():
    run_test(test_shape_art)
    
