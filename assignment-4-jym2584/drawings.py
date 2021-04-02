'''This draws the pixel based on the user color input
'''
import turtle as t
import pixart as p

def draw_pixel_color(colorstrings):
    '''Draws pixel color based on the string.
    '''
    i = 0
    isValid = True
    while i < len(colorstrings) and isValid :
        '''grabs the length of the colorstring
        '''
        color_numvalue = colorstrings[i]
        '''grabs number value and then converts it into a pixel
        '''
        if color_numvalue == "0":
            p.draw_pixel("Black")
        elif color_numvalue == "1":
            p.draw_pixel("White")
        elif color_numvalue == "2":
            p.draw_pixel("Red")
        elif color_numvalue == "3":
            p.draw_pixel("Yellow")
        elif color_numvalue == "4":
            p.draw_pixel("Orange")
        elif color_numvalue == "5":
            p.draw_pixel("Green")
        elif color_numvalue == "6":
            p.draw_pixel("Yellowgreen")
        elif color_numvalue == "7":
            p.draw_pixel("Sienna")
        elif color_numvalue == "8":
            p.draw_pixel("Tan")
        elif color_numvalue == "9":
            p.draw_pixel("Gray")
        elif color_numvalue == "A":
            p.draw_pixel("Darkgray")
        else:
            print("There is a value inside of the string that's an invalid color. Quitting...")
            isValid == False
            quit()
        i += 1

def draw_loop(number):
    '''we want to loop based on how many times the user wants the row to be
    '''
    while number > 0:
        input_colorstring = input("What's your color value? (Type any invalid color to quit): ")
        draw_pixel_color(input_colorstring)
        p.next_row()
    number -= 1

def draw_loop_input():
    inputvalue = input("Hey epic gamer (bro.. that's cringe)! How many rows do you want me to print?: ")
    draw_loop(int(inputvalue))

def main():
    p.init()
    draw_loop_input()
    t.done()

main()