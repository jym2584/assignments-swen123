'''
1. git add filename
commit the file
push the file to github
2. make the function fail and create a stub function
    make the function pass 
    refactor the code
'''
import turtle
def draw_square(color = "yellowgreen"):
    turtle.pencolor("Black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    number = 4
    while number > 0:
        turtle.forward(20)
        turtle.right(90)
        number -= 1
    turtle.forward(20)
    turtle.end_fill()

def draw_row():
    row = 2
    while row > 0:
        draw_square("green")
        draw_square("red")
        draw_square("black")
        draw_square("blue")
        draw_square("yellow")
        row -= 1

def draw_column():
    column = 10
    while column > 0:
        draw_row()
        draw_nextrow()
        print(column)
        column -= 1

def draw_nextrow():
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.backward(200)

    turtle.pendown() 

def usedasring(string):
    string_num = len(string)
    while i < string_num:
        if string_num[i] == "1":
            print(i)
        i += 1 

def main():
    turtle.tracer(0)
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pendown()
    draw_column()
    turtle.done()
main()
