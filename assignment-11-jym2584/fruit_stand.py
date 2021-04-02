class Fruit:
    #type = "Uknown"
    #price = 0
     
    __slots__ = ['type', 'price', 'count']

    def __init__(self, name, price):
        self.type = name
        self.price = price
        self.count = 0

fruits = {
    "apple":   Fruit("Apple", 1.25),
    "pear":    Fruit("Pear", 1.47),
    "grapes":  Fruit("Grapes", 2.72)}


def add_to_basket(fruit, basket):
    fruit = fruit.lower()
    if fruit in fruits:
        basket += [fruit]
        fruits[fruit].count += 1
    elif fruit == '':
        pass
    else:
        print("sorry, we don't sell ", fruit, "'s")

def total_price(basket):
    price = 0
    for item in basket:
        price += fruits[item].price
    return price

def main():
    basket = list()
    fruit = None
    while fruit != '':
        fruit = input("what fruit would you like? : ")
        add_to_basket(fruit, basket)
    

    apple_count = fruits['apple'].count
    pear_count = fruits['pear'].count
    grapes_count = fruits['pear'].count


    print("You have", apple_count, "apples", pear_count,"pears",grapes_count,"Grapes")
    print("you have", len(basket), "fruit in your basket")
    total = total_price(basket)
    print("That will be", round(total,2))



main()