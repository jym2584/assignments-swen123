'''Old code, written for naught
'''
import re

class Combo:
    drink = "None"
    entree = "None"
    side = "None"
    price = 0
    price2 = 0
    price3 = 0

combo_list = {}
combo_code = {}

def food_item():
    '''Creates the food list
    @param items, items class
    @return items, returns the item class
    '''
    items = Combo()
    items.drink = "Pepsi, Water, Tea"
    items.entree = "Burger, Rice, Mystery Meat Platter"
    items.side = "Potato Chips, French Fries, Kindle Surprise Egg"
    items.price = "1.00, 1.50, 2.00"
    items.price2 = "2.25, 5.00, 10.00"
    items.price3 = "0.99, 5.00, 200.00"
    return items

def add_to_combo_list():
    '''Adds each item to the combo list
    @param items, items class
    @param drinks, splits items.drink string into 3 seperate items
    @param drinks_price, also does the same via prices.
    @return combo_list, returns the combo list of each item
    '''
    items = food_item()
    drinks = items.drink.split(", ")
    drinks_price = items.price.split(", ")
 
    entrees = items.entree.split(", ")
    entrees_price = items.price2.split(", ")

    sides = items.side.split(", ")
    sides_price = items.price3.split(", ")

    for i in range(0,len(drinks)):
        combo_list[drinks[i]] = float(drinks_price[i])

    for i in range(0,len(entrees)):
        combo_list[entrees[i]] = float(entrees_price[i])
    
    for i in range(0,len(drinks)):
        combo_list[sides[i]] = float(sides_price[i])
    
    return combo_list

def add_list_to_combo_code():
    ''' Prints combo code for each item
    Regular expression snippet from: https://stackoverflow.com/a/25759138
    @param combo_list, grabs the dictionary of our food item list
    @return combo_code, returns the abbreviation of each item into a dictionary
    '''
    combo_list = add_to_combo_list()
    
    for key in combo_list:
        #print(key.split())
        combo_code[re.sub(r"([a-zA-Z])[a-z,A-Z]+\s*",r"\1",key).lower()] = key

    return combo_code

def order_list():
    combo_code = add_list_to_combo_code()
    combo_list = add_to_combo_list()
    items = food_item()
    #the_list = list(combo_list)
    #the_list_value = list(combo_list.values())

    drinks_list = items.drink
    entrees_list = items.entree
    sides_list = items.side
    print(drinks_list)

    #for key in combo_list:
        #print(key)
    #print("Drinks list", drinks_list)
    #print("Combo Code", combo_code)
    #print("Combo List", combo_list)
    #Accesses the meal price given an acronym
    #print(combo_list[combo_code['p']])
    return drinks_list, entrees_list, sides_list


def main():
    order_list()
main()