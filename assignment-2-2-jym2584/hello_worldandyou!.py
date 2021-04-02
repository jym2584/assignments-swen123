'''hello_world.py and hello_you.py combined into one file. 
Runs hello_world() and helloyou()
Multiline test!
Jin Moon
'''

# hello world function
def hello_world():
    ''' print hello world
    '''
    print("Hello again world!") #prints hello world

# hello you function
def helloyou():
    '''asks user for name input
    '''
    name = input("Hello, what's your name?: ") # asks for name input
    print("Hello, ", name,"!", sep="") # prints name


'''
Hello functions!
this is a multiline comment
The functions are run here
'''
hello_world()
helloyou()