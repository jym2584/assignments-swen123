"""This file creates shapes based on the user input (not sure if this is a good docstring)
"""
import turtle as t
import pixart as p

def shape_art():
    '''This gathers the user input to create various shapes
    This will pop up a message to enter shape commands
    Arguments:
        shape_command (s, r, t, d, o)
        shape_row - shape row
        shape_col - shape column
        shape_length
        shape_height
        shape_color

        Typing help on the shape command will print a list on how to draw these shapes
        eg) drawing a square: s 5 5 5 Red
    '''
    t.tracer(False)
    no_quit = True
    input("Enter a shape command or 'exit'...\n   (i) Seperate each input by spaces. Type help for more info.\n\nPress enter to continue...")
    #print(shape_commands)
    #print("ZE MESSAGE", message)
    while no_quit == True: # While the program is still active
        message1 = input("Shape command: ") # Ask the user what the shape command is
        tokens = message1.split(" ")
        shape_command = tokens[0]
        if message1 == "quit" or message1 == "exit" or message1 == "": # If the user types any of the 3, it will prompt them to press enter to exit the command, or enter any...
            message1 = input("Press enter to exit or press any key to resume typing the shape command...")                  #... character to resume typing the shape command.
            if message1 == "":
                no_quit = False
                break #This quits the program
        elif message1 == "erase": # This erases the entire turtle draw if erase is typed
            p.init(False)
        elif message1 == "help": # This prints out the arguments required to make the shapes draw
            input("Arguments required for each shapes:\n   1. Square s row column length color\n   2. Rectangle: r row column length height color\n   3. Triangle: t row column height color \n   5. Diamond: d row column height color\n   6. Octagon: o row column length color\n\nOther:\n   erase - erases everything\nPress enter to return...")
        elif shape_command == "s": # Square
            shape_row = int(tokens[1])
            shape_col = int(tokens[2])
            shape_length = int(tokens[3])
            shape_color = tokens[4]
            p.draw_square(shape_row, shape_col, shape_length, shape_color)
        elif shape_command == "r": # Rectangle
            shape_row = int(tokens[1])
            shape_col = int(tokens[2])
            shape_length = int(tokens[4])
            shape_height = int(tokens[3])
            shape_color = tokens[5]
            p.draw_rectangle(shape_row, shape_col, shape_height, shape_length, shape_color)
        elif shape_command == "t": # Triangle
            shape_row = int(tokens[1])
            shape_col = int(tokens[2])
            shape_height = int(tokens[3])
            shape_color = tokens[4]
            p.draw_triangle(shape_row,shape_col,shape_height,shape_color)
        elif shape_command == "d": # Diamond
            shape_row = int(tokens[1])
            shape_col = int(tokens[2])
            shape_height = int(tokens[3])
            shape_color = tokens[4]
            p.draw_diamond(shape_row,shape_col,shape_height,shape_color)
        elif shape_command == "o": # Octagon
            shape_row = int(tokens[1])
            shape_col = int(tokens[2])
            shape_length = int(tokens[3])
            shape_color = tokens[4]
            p.draw_octagon(shape_row,shape_col,shape_length,shape_color)
        else: # If the command is invalid, we notify the user that the command is invalid.
            input("This shape or command is invalid. Enter any key to return.")
            
def parse_command(triangle):
    '''Testing tokens
    '''
    tokens = triangle.split(" ")
    row = int(tokens[0])
    col = int(tokens[1])
    height = int(tokens[2])
    color = tokens[3]
    p.draw_triangle(row, col, height, color)

def inputsomething():
    command = input("enter something")
    parse_command(command)

#inputsomething()
shape_art()