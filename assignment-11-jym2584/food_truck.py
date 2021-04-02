import re

class Combo:
    drink = "None"
    entree = "None"
    side = "None"
    price = 0

# Create a menu with drinks, entree, side with price
# Edit add_list_to_combo_code to abbreviate food_menu
# Menu should include 24 combos (for 3 items on each combo), iterate through drinks, entree and side to create possible combos

price_list = {"Pepsi": 1.00, "Water": 1.50, "Tea": 2.00, 
            "Burger": 2.25, "Rice": 5.00, "Mystery Meat Platter": 2.00,
            "Potato Chips": 0.99, "French Fries": 5.00, "Kindle Surprise Egg": 200.00}


def create_abbreviations():
    ''' Prints combo code for each item
    Regular expression snippet from: https://stackoverflow.com/a/25759138

    @param combo_list, grabs the dictionary of our food item list
    @return combo_code, returns the abbreviation of each item into a dictionary
    '''
    food_menu_abbrv = {}
    
    for key in price_list:
        #print(key.split())
        food_menu_abbrv[re.sub(r"([a-zA-Z])[a-z,A-Z]+\s*",r"\1",key).lower()] = key

    return food_menu_abbrv

def menu():
    '''Creates the menu dictionary
    @return food_menu, returns the dictionary
    '''
    food_menu = {
        "drinks": ["Pepsi", "Water", "Tea"], 
        "entrees": ["Burger", "Rice", "Mystery Meat Platter"], 
        "sides": ["Potato Chips", "French Fries", "Kindle Surprise Egg"]
    }
    return food_menu

def print_menu():
    '''Prints the food menu
    '''
    food_menu_abbrv = create_abbreviations()
    
    print("**MENU**\nAll meals are a combo!\n--------------------------")
    
    print("Drinks\n",
    "Pepsi (p): $", price_list[food_menu_abbrv["p"]], "     ", "Water (w): $", price_list[food_menu_abbrv["w"]], "     ", "Tea (t): $", price_list[food_menu_abbrv["t"]], "\n",
    sep="")
    
    print("Entrees\n",
    "Burger (b): $", price_list[food_menu_abbrv["b"]], "     ", "Rice (r): $", price_list[food_menu_abbrv["r"]], "     ", "Mystery Meat Platter (mmp): $", price_list[food_menu_abbrv["mmp"]], "\n",
    sep="")
    
    print("Sides\n",
    "Potato Chips (pc): $", price_list[food_menu_abbrv["pc"]], "     ", "French Fries (ff): $", price_list[food_menu_abbrv["ff"]], "     ", "Kindle Surprise Egg (kse): $", price_list[food_menu_abbrv["kse"]], "\n",
    sep="")

def order_combo():
    '''Inputs for ordering
    @param food_menu_abbrv, grabs abbreviations from inputs
    @param food_menu, checks to see if the input exists on the food menu
    @param order, our combo class
    @param valid_drink, Will always ask for the same input if the item is not on the menu
    @param current_combo, adds the combo to the list
    
    @return current_combo, returns the combo as a list
    '''
    food_menu_abbrv = create_abbreviations()
    food_menu = menu()
    order = Combo()

    valid_drink = False
    valid_entree = False
    valid_side = False

    # Repeats input until a valid drink is chosen
    while valid_drink == False:
        drink = input("What would you like to drink: ")
        try:
            if food_menu_abbrv[drink] in food_menu["drinks"]:
                order.drink = food_menu_abbrv[drink]
                valid_drink = True
        except:
            print("That drink isn't on the list! Drinks: Pepsi (p), Water (w), Tea (t)")

    # Repeats input until a valid entree is chosen
    while valid_entree == False:
        entree = input("What entree would you like: ")
        try:
            if food_menu_abbrv[entree] in food_menu["entrees"]:
                order.entree = food_menu_abbrv[entree]
                valid_entree = True
        except:
            print("That entree isn't on the list! Entrees: Burger (b), Rice (r), Mystery Meat Platter (mmp)")

    # Repeats input until a valid side is chosen
    while valid_side == False:
        side = input("What would you like as a side: ")
        try:
            if food_menu_abbrv[side] in food_menu["sides"]:
                order.side = food_menu_abbrv[side]
                valid_side = True
        except:
            print("That side isn't on the list! Sides: Potato Chips (pc), French Fries (ff), Kindle Surprise Egg (kse)")

    order.price = price_list[food_menu_abbrv[drink]] + price_list[food_menu_abbrv[entree]] + price_list[food_menu_abbrv[side]]

                #Item Name             #The price of the item
    print("  Combos chosen: ", order.drink, " ($", price_list[food_menu_abbrv[drink]],")", ", ", order.entree, " ($", price_list[food_menu_abbrv[entree]],")",", ", order.side, " ($", price_list[food_menu_abbrv[side]],")", sep="")
    
    print("  Current price:", order.price)

    current_combo = [food_menu_abbrv[drink], food_menu_abbrv[entree], food_menu_abbrv[side]]
    return current_combo

def take_order():
    '''Asks for input if they want to add another combo
    @param ask_input, asks if they want another combo
    @param order, our pretty list for the order
    @return order, all the order combos, if added
    '''
    order = []
    current_combo = order_combo()
    order.append(current_combo)
    ask_input = input("Do you want to add another combo? (Y for yes. Press enter any other key to stop ordering.)")
    while ask_input.lower() == "y":
        order.append(order_combo())
        #print("Current order: ", order)
        ask_input = input("Do you want to add another combo? (Y for yes. Press enter any other key to stop ordering.)")
    return order

def print_order():
    ''' Prints the current combo and price
    @param order, takes the order
    @param price, adds up the price of each order
    '''
    order = take_order()
    price = 0
    print("Your current combos: ", end="")
    for each_order in order:
        print()
        for items in each_order:
            print(items, end = "")
            print("", end = " ", sep = "")
            price += price_list[items]
    print("\nTotal:", price)
    print("Thanks for visiting us! Never leave hungry")

def main():
    print_menu()
    print_order()
    pass

if __name__ == "__main__":
    main()