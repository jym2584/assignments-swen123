import memory
import cards
from testing import *

testing = True

def test_make_flippable():
    #setup
    card = cards.make_deck()
    #invoke
    function = memory.make_flippable(card)
    truefalse = function[0]
    #analyze
    assert_equals("False?", False, truefalse)

def test_ismatch():
    ## setup
    deck = cards.make_deck()
    deck2 = cards.make_deck()

    flippable = memory.make_flippable(deck[0]) # Accessing first card of the deck
    flippable2 = memory.make_flippable(deck2[0]) # Also the same for testing purposes
    
    print("\nLets check the cards if they're the same")
    print(flippable)
    print(flippable2)
    # Are they false?
    print("Are the cards false?")
    print(flippable[0])
    print(flippable2[0])

    print("Let's set them to True")
    flippable[0] = True # Let's set them equal to true!
    flippable2[0] = True

    ## invoke
    isequal = memory.ismatch(flippable,flippable2)

    ## analyze
    assert_equals("Are the cards facing up and the same?", True, isequal)

def test_select_cards():
    #setup
    number = 10
    deck = cards.make_deck()

    #invoke
    same_cards = memory.select_card(number,deck)
    same_cards.sort() # Let's sort them to test if they're the same
    print()
    for i in range(len(same_cards)):
        print(same_cards[i][3], end= " ") # Printing the cards via shorthand
    print()
    ## analyze - Making sure that they're the same via name
    assert_equals("Are they the same?", same_cards[0][2], same_cards[1][2]) # I don't know how to do a test for this but I sorted them and made sure index 0 and 1 are the same.

def run_all_tests():
    run_test(test_make_flippable)
    run_test(test_ismatch)
    run_test(test_select_cards)

run_all_tests()
