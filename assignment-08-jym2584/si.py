"""
1. Create a function that takes names from the user until an empty string is inputted. Each name should be inputted into one big list.
2. Create a function that for each name in the list breaks the name up into characters and places the characters of the name into a tuple (each name will have its' own tuple).
The function should take a parameter, name_list. Make a new list of the tuples and return it.
3. Create a function that prints a welcome message to every name that was provided by iterating through the tuple of characters and printing them.
The function should take the list of tuples as a parameter. Each welcome message should print on a new line but should be contained to only 1 line.
"""

def grab_name():
    names = []
    name = input("Enter a name: ")
    while name != "":
        names.append(name)
        name = input("Enter a name: ")
    return names

def break_names(name_list):
    tuple_list = []
    for item in name_list:
        tuple_list.append(tuple(item))
    return tuple_list

def welcome_message(tuple_list):
    for i in range(len(tuple_list)):
        print("Welcome ", end="")
        name= tuple_list[i]
        for char in name:
            print(char, sep="", end="")
        print()


def main():
    names = grab_name()
    name_tuples = break_names(names)
    welcome_message(name_tuples)
main()