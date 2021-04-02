    import cards
from testing import *
import random

def test_cards():
    rank = 2
    suit = "Hearts"
    card = cards.make_card(rank, suit)
    assert_equals("card", cards.make_card(2, "Hearts"), card)

def test_make_deck():
    actual = cards.make_deck()
    assert_equals("Length", 52, len(actual))
    assert_equals("the deck", "2 of Diamonds", actual[1][2])

def test_shuffle():
    #setup
    random.seed(1)
    make_a_list = cards.make_deck()
    
    #invoke
    actual = cards.shuffle(make_a_list)

    print("\n\nStart of shuffled cards list:\n----------------")
    for i in range(len(actual)):
        print(actual[i][2], end=" | ")
    print("\n----------------\nEnd of shuffled cards list\n")

    #test
    assert_equals("|| index 0 should not be 2 of hearts ||", "7 of Hearts", actual[0][2])

def test_draw():
    #setup
    random.seed(1)
    deck = cards.shuffle(cards.make_deck())

    #invoke
    actual = cards.draw(deck)
    #analyze
    assert_equals("Card taken out is now on the hand", "Queen of Hearts", actual[2])

def test_deal():
    #setup
    random.seed(1)
    deck = cards.shuffle(cards.make_deck())
    number = 8

    #invoke
    actual = cards.deal(deck,number)
    num = len(actual)
    print(num)
    #analyze
    assert_equals("Test", 2, num)

def run_all_tests():
    run_test(test_cards)
    run_test(test_make_deck)
    run_test(test_shuffle)
    run_test(test_draw)
    run_test(test_deal)

run_all_tests()