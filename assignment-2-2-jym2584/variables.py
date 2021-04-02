def variable_practice():
    '''x and y variables
    '''
    x = int(input ("Enter a number!: ")) # number 1
    y = int(input ("Enter another number!: ")) # number 2
    arithmetic(x, y)

def arithmetic(x,y):
    ''' Added math here
    '''
    print("Addition: ", x, " + ", y, " = ", x + y, #addition
    "\nSubtraction: ", x, " - ", y, " = ", x - y, #subtraction
    "\n Division: ", x, " / ", y, " = ", x/y, sep="") #division

variable_practice() #runs variable_practice