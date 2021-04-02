'''
Date Type   Complexity Access/Update    Complexity Insert/Delete    Is orderable    Values must be unique
---------   ------------------------    ------------------------    ------------    ---------------------
Array       O(c)                        N/A                         Yes             No
Python List O(c)                        O(n). O(c) at the end       Yes             No
Dictionary  O(c)                        O(c)                        No              Keys are unique
Set         N/A                         O(c)                        No              Yes
Stack       O(c) from the top only      O(c) for push and pop       Is Ordered      No
                                                                    (occur on a specific order, implicit order)
Queue       O(c)                        O(c)                        Is Ordered      No
'''

import random
import array_queue
import node_stack

class Grocery:

    __slots__=["__name", "__weight", "__price"]

    def __init__(self, number):
        self.__name = "Item #" + str(number)
        self.__weight = random.randint(1,10)
        self.__price = random.randint(1,20)

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price

    def __repr__(self):
        return "{} {}lb ${:.2f}".format(self.__name, self.__weight, self.__price)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__name == other.__name and self.__weight == other.__weight
        else:
            return False
    
    def __hash__(self):
        return hash(self.__name) * 31 + self.__weight

    def __lt__(self, other):
        return self.__name < other.__name

def fill_store(number):
    a_store = {}
    for i in range(number):
        grocery = Grocery(i)
        a_store[grocery.get_name()] = grocery
    return a_store

class Customer:

    __slots__ = ["__shopping_list", "__cart", "__bags"]

    def __init__(self, list_of_names):
        self.__cart = set()
        self.__bags = []

        random.shuffle(list_of_names)
        self.__shopping_list = list(list_of_names[:26])

    def get_bags(self):
        return self.__bags
    
    def shop(self, store):
        for name in self.__shopping_list:
            self.__cart.add(store[name])

    def unload(self):
        belt = array_queue.Queue()
        for item in self.__cart:
            belt.enqueue(item)
        return belt
    
    def unpack(self):
        for bag in self.__bags:
            while not bag.is_empty():
                removed = bag.pop()
                print(removed)

def cashier(belt, customer):
    total_price = 0
    while not belt.is_empty():
        item = belt.dequeue()
        total_price += item.get_price()
        bagged = False
        for bag in customer.get_bags():
            if item.get_weight() <= bag.peek().get_weight():
                bag.push(item)
                bagged = True
                break
        if bagged == False:
            bag = node_stack.Stack()
            bag.push(item)
            customer.get_bags().append(bag)
    return total_price


def main():
    a_store = fill_store(100)
    customer = Customer(list(a_store.keys()))
    customer.shop(a_store)
    belt = customer.unload()
    print("That will be $", cashier(belt, customer), sep ="")
    customer.unpack()
if __name__ == "__main__":
    main()