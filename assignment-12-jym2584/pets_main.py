from pets import *


def main():
    try:
        corgi = Pet("Snuffles", 2, "Dog", "Yellow")
        #print(corgi.__name, corgi.__weight)
        corgi.feed(1800)
        corgi.walk(1.5)
        print(corgi.get_name())
        print(round(corgi.get_weight(),3))
    except AttributeError:
        print("You cannot access an attribute!")

main()