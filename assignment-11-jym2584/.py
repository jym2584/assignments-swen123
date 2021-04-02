class Topping:
    '''Class for toppings
    '''
    __slots__ = ['code', 'name', 'price']

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Pizza:
    '''Class for our pizza
    '''
    __slots__ = ['price', 'cheese', 'veggies', 'meat']

    def __init__(self):
        self.price = 5.0
        self.cheese = 's'
        self.veggies = []
        self.meat = []

# Our toppings!
cheese = {'s': Topping('s', "Swiss Cheese", 0.0),
          'b': Topping('b', "Blue Cheese", 1.5),
          'c': Topping('c', "Cheddar", 5.0)}
    
meats = {'p': Topping('p', "Pepperoni", 10.15),
          'h': Topping('h', "Hamburger", 2.5),
          'cf': Topping('cf', "Chicken Fingers", 3.0),
          'n': Topping('n', "None", 0.0)}

veggies = {'p': Topping('p', "Pineapple", 0.75),
          'm': Topping('m', "Mushrooms", 5.25),
          'a': Topping('a', "Apples", 0.50),
          'n': Topping('n', "None", 0.0)}
# End of our toppings

def print_menu(topping, str_topping):
    '''Pizza de menu (Pizza menu); prints a topping given a key and string
    @param topping, grabs the dictionary
    @param str_topping, the toppping's name as a string (because I don't know how to execute topping as just a string instead of it printing as a dictionary)
    '''
    print("\n  | ", str_topping, " Options:", sep="")
    print("  | ", end = "")
    for key in topping:
        print(topping[key].name, " (",topping[key].code,"): ", "$",topping[key].price, sep="", end = "     ")
    print()

def order_pizza():
    '''Ordering our toppings!
    @param select, selecting our current topping. Returns false if they select one or more toppings
    @param ask, input for asking the user to pick a cheese 
    @param pizza_count, used to loop asking for toppings until we finish 2 pies!
    @param pizzas, dictionary for our 2 pizza classes
    @param tokens, splits the prompt up if multiple toppings are selected

    @return pizzas, returns the 2 dictionary keys (pizzas) that contains our toppings!

    '''

    pizzas = {'1': Pizza(),
              '2': Pizza()}

    prices_init = 0
    pizza_count = 1
    select_cheese = True
    select_meat = True
    select_veggie = True

    while pizza_count < 3:
        print("For your pizza #",pizza_count,"....", sep="")

        ## Choosing our Cheese ##
        while select_cheese:
            ask = input("> Choose one type of cheese (O for options): ")

            if ask.lower() == "q": # If the user types q. The entire command prompt shuts down.
                print("Quitting.... (BRO DONT GO)")
                quit()
            try:
                if ask.lower() == "o": # Else if they ask for options, it will print the options menu
                    print_menu(cheese, "Cheese")
                    print()

                elif ask.lower() == cheese[ask].code: # Else if a cheese is valid, choose that as our topping
                    pizzas[str(pizza_count)].cheese = cheese[ask].code # Adds the cheese code to our pizza class
                    pizzas[str(pizza_count)].price += cheese[ask].price # Sums up the current cost of our pizza
                    select_cheese = False # We have selected our cheese!
            
            except: # If the cheese is not valid, alter the user that the cheese doesn't exist
                print("  (!) Not a valid type of cheese.") 
                #print_menu(cheese, "Cheese")
                print()

        ## Choosing our meat ##
        while select_meat:
            ask = input("> Choose your meats (O for options): ")
            tokens = ask.lower().split(" ") # Will be used for more than 1 toppings
            
            try:
                if ask.lower() == "o": # If they ask for options, it will print the options menu
                    print_menu(meats, "Meat")
                    print()

                else: # Else, it will print the selected toppings
                    for i in tokens: # Checking if more than 1 toppings are selected
                        pizzas[str(pizza_count)].meat.append(meats[i].code) # Adds the meat code to our pizza class
                        prices_init += meats[i].price # Sums up the current cost of our pizza, as long as it's valid

                    select_meat = False # We have chosen our meat toppings!
                    pizzas[str(pizza_count)].price += prices_init # Let's charge our customer for the (valid) meat toppings chosen.
            
            except: # If the topping is not on the list, clear the list and make them try again.
                print("  (!) Not a valid type of meat. Selection cleared, try again.")
                pizzas[str(pizza_count)].meat.clear() # Clears the list given an invalid selection
                prices_init = 0 # Setting our topping balance back to 0 because an invalid selection was chosen.
                print()

        ## Choosing our veggie ##
        while select_veggie:
            prices_init = 0 # Resetting the prices for our veggies.

            ask = input("> Choose your veggies. (O for options): ")
            tokens = ask.lower().split(" ")

            try:
                if ask.lower() == "o": # If they ask for options, it will print the options menu
                    print_menu(veggies, "Veggie")
                    print()

                else: # Else, it will print the selected toppings
                    for i in tokens: # Checking if more than 1 toppings are selected
                        pizzas[str(pizza_count)].veggies.append(veggies[i].code) # Adds the veggies code to our pizza class
                        prices_init += veggies[i].price # Sums up the current cost of our pizza, as long as it's valid
                    
                    print()

                    select_veggie = False # We have chosen our veggies!
                    pizzas[str(pizza_count)].price += prices_init # Let's charge our customer for the (valid) veggie toppings chosen.
            
            except: # If the topping is not on the list, alert the user
                print("  (!) Not a valid type of veggie. Selection cleared, try again.")
                pizzas[str(pizza_count)].veggies.clear() # Clears the list given an invalid selection
                prices_init = 0 # Setting our topping balance back to 0 because an invalid selection was chosen.
                print()

        pizza_count += 1 # Let's go add toppings for our second pizza!
        select_cheese = True # Set all of these back to true for our second pizza
        select_meat = True
        select_veggie = True
    return pizzas # Returns the dictionary of both of our pizza 1 and 2 keys 

def print_pizzas(pizza):
    ''' Prints the pizza in an efficient (but not-so-efficient i think[rip time complexity n^3]) way
    @param total, adds up the sum of the subtotal cost of our pizzas
    '''
    total = 0
    print("\n\n\nYour Order")

    for i in range(1, len(pizza)+1): # For every pizza (first and second))
        print("  One pizza with:", "\n",
            "    - Cheese: ", cheese[pizza[str(i)].cheese].name, sep="")    # Prints ordered cheese

        print(
            "    - Meats: ", end="", sep="")
        for meat_code in pizza[str(i)].meat:
            print(meats[meat_code].name, end=" ", sep=" ")                  # Prints ordered meats

        print()

        print(
            "    - Veggies: ", end="", sep="")
        for veggie_code in pizza[str(i)].veggies:
            print(veggies[veggie_code].name, end=" ", sep="")               # Prints ordered veggies

        print()

        print(
            "-------------------------------","\n",
            " Pizza ",i," Subtotal: $", pizza[str(i)].price, "\n", sep="")  # Adds the subtotal
        
        total += pizza[str(i)].price

    print("===============================")
    print(" > Total:", total, "\n\n\n")                                     # Adds the total

def main():
    ''' Our main function used to run the pizzaria
    '''
    # Pizza 1: s p p
    # Pizza 2: b h m
    print("""
                          _   _      _____    _                              ____
     /\                  (_) (_)    |  __ \  (_)                            /    \	
    /  \     ___    ___   _   _     | |__) |  _   ____  ____   __ _           u  u|      _______
   / /\ \   / __|  / __| | | | |    |  ___/  | | |_  / |_  /  / _` |            \ |  .-''#%&#&%#``-.   
  / ____ \  \__ \ | (__  | | | |    | |      | |  / /   / /  | (_| |           = /  ((%&#%&#%&#%&#%))  
 /_/    \_\ |___/  \___| |_| |_|    |_|      |_| /___| /___|  \__,_|            |    `-._#%&##&%_.-'   
                                                                             /\/\`--.   `-."".-'
_________________________________________________________________________    |  |    \   /`./      
                                                                             |\/|  \  `-'  /
 Welcome to Asscii Pizzaria, where we serve the best pizzas in Rochester     || |   \     /   
Base price of one pizza is $5   We only serve orders for 2 (best) pizzas
_________________________________________________________________________   
""")
#
    pizzas = order_pizza()
    print_pizzas(pizzas)

    print("""
                     _____
                    (     )
                     |   |
                     |   |
Thanks for coming! (◕ ‿ ◕ ✿)
(Bro that's cringe)
    """)
if __name__ == "__main__":
    main()