'''This is main function where we initialize and draw our pixels
'''
import turtle as t

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

def init(tracer_on = True):
    t.reset()
    t.tracer(tracer_on)
    t.speed(0)
    t.pencolor("Black")
    t.fillcolor("White")
    t.penup() # abbreviation for t.penup()
    t.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)

def show():
    t.tracer(True)

def move (row,column):
    x = column * PIXEL_SIZE - PIXEL_SIZE * COLUMNS / 2
    y = PIXEL_SIZE * ROWS / 2 - row * PIXEL_SIZE
    t.goto(x,y)

def draw_row(row, column, num_pixels, col = "Red"):
    move(row,column)
    # or for _ in range:
    for i in range (num_pixels):
        draw_pixel(col)

def draw_rectangle(row, column, height, width, color = "Orange"):
    '''Draws the rectangle
    '''
    for i in range(0, height):
        draw_row(row + i, column, width, color)

def draw_square(row, col, side, color = "Green"):
    '''Draws the square
    '''
    for i in range(0, side):
        draw_row(row + i, col, side, color)

def draw_triangle(row, col, height, color = "Red"):
    '''Draws the triangle
    '''
    width = 1
    for i in range(0, height):
        draw_row(row, col, width, color)
        width += 2
        row += 1
        col -= 1

def draw_diamond(row, col, height, color = "Purple"):
    '''Draws the diamond
    '''
    width = 1
    if (height % 2) == 0:
        for i in range(0, round(height/2)):
            draw_row(row, col, width, color)
            width += 2
            row += 1
            col -= 1
        for i in range(0,round(height/2)):
            draw_row(row, col + 1, width - 2, color)
            row += 1
            width -= 2
            col += 1
    else:
        for i in range(0, round(height/2)):
            draw_row(row, col, width, color)
            width += 2
            row += 1
            col -= 1
        for i in range(0,round(height/1.5)):
            draw_row(row, col, width, color)
            row += 1
            width -= 2
            col += 1

def draw_octagon(row, col, side, color = "Cyan"):
    '''Draws the octagon
    '''
    width = side
    for i in range(0, side):
        draw_row(row, col, width, color)
        width += 2
        row += 1
        col -= 1
    for i in range(4,4+round(side/2)):
        draw_row(row, col + 1, width - 2, color)
        draw_row(row + 1, col + 1, width - 2, color)
    for i in range(0,side):
        draw_row(row + 2, col + 1, width - 2, color)
        row += 1
        width -= 2
        col += 1







def next_row():
    ''' This moves the turtle to the next row if called
    '''
    ycor = t.ycor() - PIXEL_SIZE
    t.setpos(-COLUMNS/2*PIXEL_SIZE, ycor)



def draw_pixel(color):
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()

    counter = 4
    while counter > 0:
        t.forward(PIXEL_SIZE)
        t.right(90)
        counter -= 1

    t.penup()
    t.end_fill()
    t.forward(PIXEL_SIZE)

def main():
    init(False)
    #draw_rectangle(3,3,6,14)
    #draw_square(5,6,8)
    #draw_triangle(5,10,8)
    draw_diamond(5,10,9)
    #draw_octagon(5,8,4)
    #draw_row(2,2,5)
    #move(6,6)
    t.done()

if __name__ == "__main__":
   main()