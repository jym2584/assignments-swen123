'''Pixart.py Test
'''
import turtle as t
import pixart as p
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

def assertle(x_cor, y_cor, color, tracer_on = True):
    assert_equals("speed", 0, t.speed())
    assert_equals("pen down", False, t.isdown())
    assert_equals("xcor", x_cor, round(t.xcor(),0))
    assert_equals("ycor", y_cor, round(t.ycor(),0))
    assert_equals("pen color", "Black", t.pencolor())
    assert_equals("fill color", color, t.fillcolor())
   # assert_equals("Tracer", tracer_on, t.tracer())



def test_init_tracer_on():
# Setup
#Invoke
    p.init(False)
#Analyze
    assertle(-300,300, "White", False)

def test_show():
    #Setup
    p.init(False)
    #Invoke
    p.show()
    #analyze
    assertle(-300,300, "White", True)

def test_draw_row():
    #Setup
    p.init()
    #Invoke
    p.draw_row(2,2,4)
    #Analyze
    assertle(-120,240,"Red")

def test_draw_rectangle():
    #setup
    p.init(False)
    #invoke
    p.draw_rectangle(2,2,3,4)
    #analyze
    assertle(-120,180,"Orange")

def test_draw_square():
    #setup
    p.init(False)
    #invoke
                #row,col,side
    p.draw_square(5,6,8)
    #analyze
    assertle(120,-60,"Green")

def test_draw_triangle():
    #setup
    p.init(False)
    #invoke
                #row,col,height
    p.draw_triangle(5,10,8)
    #analyze
    assertle(240,-60,"Red")

def test_draw_diamond():
    #setup
    p.init(False)
    #invoke
                #row,col,height
    p.draw_diamond(5,10,9)
    #analyze
    assertle(60,-60,"Purple")

def test_draw_octagon():
    #setup
    p.init(False)
    #invoke
                #row,col,side
    p.draw_octagon(5,8,4)
    #analyze
    assertle(60,-120,"Cyan")




def test_move():
    #Setup
    p.init()
    #Invoke
    p.move(2,2)
    #Analyze
    assertle(-240,-240, "White")





def run_all_tests():
    run_test(test_draw_rectangle)
    run_test(test_draw_square)
    run_test(test_draw_triangle)
    run_test(test_draw_diamond)
    run_test(test_draw_octagon)

    #test_draw_row()
    #run_test(test_init)
     #run_test(test_draw_blackpixel)
    #run_test(test_draw_redpixel)
   # run_test (test_show)
   # run_test(test_init_tracer_on)
    #run_test(test_move)

if __name__ == "__main__":
   run_all_tests()
