from testing import *
import blackjack as b
import cards as c
import random

def test_hand_score():
    random.seed(1)
    deck = c.shuffle(c.make_deck())
    hand1, hand2 = c.deal(deck, 2)

    #invoke
    hand1_score = b.hand_score(hand1)
    hand2_score = b.hand_score(hand2)
    print("Scores", hand1_score, hand2_score)
    #analyze:
    assert_equals("Hand 1 score", 15, hand1_score)
    assert_equals("Hand 2 score", 12, hand2_score)


def run_all_tests():
    run_test(test_hand_score)
run_all_tests()