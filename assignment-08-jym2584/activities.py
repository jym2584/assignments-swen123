import random
import cards

def tuples(a_tuple):
    print("Number of tuples", len(a_tuple))
    for i in a_tuple: # did for i in range(len(a_tuple)) instead
        print("Tuple Element", i) # did a_tuple[i] instead
    #a_tuple[2] = 3 # Gives out a typeerror when trying to change elements using index

def lists():
    
    lista = [3, 5.4, "Pi", True, (3,'b')]
    for i in range(len(lista)):
        print(i,": ", lista[i], sep="")
    lista[3] = False
    return lista

def make_list(a_sequence):
    a_list = []
    for i in a_sequence:
        a_list.append(i)
        #print(a_list)
    return a_list

def scale(a_list, scalar):
    #for i in a_list: # Multiplying number by scalar, not list by number 
        #i *= scalar
    for i in range(len(a_list)):
        a_list[i] *= scalar

def mutater(a_list, an_int):
    print("A list and int before:", a_list, an_int)
    an_int *= 4
    a_list[0] *= 4
    print("A list and int after:", a_list, an_int)

def cat(a_list, b_list):
    the_list = a_list + b_list
    return the_list

def extend(a_list, b_list):
    a_list = a_list + b_list
    return a_list

def extender(a_list, b_list):
    a_list += b_list
    return a_list

def tuple_equality(tuple1, tuple2):
    print(tuple1, tuple2)
    print(tuple1 is tuple2)
    print(tuple1 == tuple2)

def reverse_sequence(sequence):
    list = []
    for i in range(len(sequence)-1, -1, -1): # Reverse order
        list.append(sequence[i])

    return list

def slicing(a_sequence):
     a_list = list(a_sequence)
     start = 0
     for i in range(len(a_list)):
         if a_list[i] == ' ':
             print(a_list[start:i])
             start = i + 1
     print(a_list[start:])

def dices(a_list):
    if a_list == []:
        pass
    else: 
        print(a_list[0:1])
        dices(a_list[1:])

def random_list(size):
    a_list = []
    for _ in range(size):
        a_list += [random.randint(0,size)]
    return a_list

def sorted_test(a_list):
    print("Before", a_list)
    sort = sorted(a_list, reverse=True)
    print("After", sort)

    return sort

def sort_test(a_list):
    print(a_list)
    sort = a_list.sort(reverse = True)
    print(a_list, sort)

def print_hand(hand):
    for card in hand:
        print(card[3], end = " ")
    print()

def sort_cards():
    deck = cards.make_deck()
    cards.shuffle(deck)
    hand1, hand2 = cards.deal(deck, 5)

    print()
    print_hand(hand1)
    print_hand(hand2)

    hand1.sort(key=suit_key)
    hand2.sort(key=suit_key)

    print()
    print_hand(hand1)
    print_hand(hand2)

def suit_key(card):
    card_value = card[0]
    if card[1] == "Clubs":
        card_value += 100
    elif card[1] == "Diamonds":
        card_value += 200
    elif card[1] == "Hearts":
        card_value += 300
    else:
        card_value += 400
    
    return card_value

def main2():
     #slicing("This is a sentence!")
     #a_list = [1,2,3,4,5]
     #dices(a_list)
     #dices(list("This is a sentence!"))
     #sorted_test(random_list(10))
     #sort_test(random_list(10))
     #######################################
    sort_cards()

if __name__ == "__main__":
    main()
    main2()


def main():
    #a_lists = lists()
    #print(a_lists)
    #a_sequence = "abc"
    #make_list(a_sequence)
    #a_list = make_list(range(1,4))
    #print(a_list)
    #scale(a_list, 5)
    #print(a_list)
    #a_list = [2]
    ##an_int = 3
    #print(a_list, an_int)
    #mutater(a_list, an_int)
    #print(a_list,an_int)
    #a_list = [1,2,3]
    #b_list = [4,5,6]
    #c_list = cat(a_list, b_list)
    #c_list = extend(a_list, b_list)
    #print(a_list, b_list, c_list)
    #print(extender(a_list, b_list))
    ##################################
    #a_list = [2, 5, 7, 9]
    
    #tuple1 = tuple(a_list)
    #tuple_equality(tuple1, tuple1) # True because they're both referring to the list
    
    #tuple2 = tuple(a_list)
    #tuple_equality(tuple1, tuple2) # Eventhough they have the same values, they're technically different tuples

    #tuple3 = tuple([1, 2, 3, 4, 5])
    #tuple_equality(tuple1, tuple3) # False.
    ##################################
    #a_list = [1,2,3,4]
    #print(reverse_sequence("Hello Word"))
    
    #s = "Hello World"
    #print(s[2:4]) # prints ll
    #print(s[:5]) # Prints hello, there is no start
    #print(s[6:]) # Prints World, there is no end
    #rint(s[::-1]) # Prints dlroW olleH
    #print(s[6::-1]) # Prints W olleH
    #print(s[6:6]) # Prints nothing
    #print(s[6:60000000000000000]) # Prints World
    #print(s[-600000000000:6000000000000]) # Prints Hello World
    pass