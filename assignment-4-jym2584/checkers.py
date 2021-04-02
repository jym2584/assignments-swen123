'''Draws checkers that is determined on inputted rows and columns
'''
import turtle as t
import pixart as p

def draw_checkers(column,row):
    ''' Draws a checker
        Want to check if ROWS = 20, then we print red, black until it reaches 20
        Want to check if COLUMNS = 20, then we print black, red until it reaches 20
    '''
    ROW = row
    column_init = column # We want to initialize the inputted value for column
    while ROW > 0:
        ''' We want to check the amount of rows defined before it stops drawing.
        Let row = 10
        '''
        if ROW % 2 == 0: 
            '''This sets up the very first row!
            If the row is even (10) then we print out the row red and black
            '''
            while column > 0:
                '''This determines the amount of columns we should print. If column = 10, then there should be 10 columns by the end result
                1. If the column is red and even, then we print out the amount of columns defined
                2. Otherwise we print out black
                '''
                is_red = True 
                if is_red and column % 2 == 0: # We want to make sure that the color is red and the column is even before printing the red pixel.
                    p.draw_pixel("red")
                else: # Otherwise we should draw the black pixel
                    p.draw_pixel("black")
                is_red = False
                column -= 1 # This subtracts the amount of columns which now becomes an odd value. This keeps on printing red and black until column becomes 0
        
            column = column_init # This sets back the columns to the initialized value so we can print 10 more columns on the next row!
        else:
            '''Now that the row value is odd (9) then we print out 10 black and red squares on the next row!
            '''
            while column > 0:
                is_black = True
                print(column)
                if is_black and column % 2 == 0:
                    p.draw_pixel("black")
                else:
                    p.draw_pixel("red")
                is_black = False
                column -= 1
                
            column = column_init # This sets back the columns to the initialized value so we can print 10 more columns on the next row!
        next_row() # Since the row isn't 0 yet, we should go on to the next row!

        ROW -= 1 # This subtracts the row from 10 to 9 until it reaches 0!


def next_row():
    ''' This moves the turtle to the next row if called
    '''
    ycor = t.ycor() - p.PIXEL_SIZE
    t.setpos(-p.COLUMNS/2*p.PIXEL_SIZE, ycor)

def main():
    p.init()
    
    draw_checkers(20,20) # Column, Row
    t.done()

if __name__ == "__main__":
   main()