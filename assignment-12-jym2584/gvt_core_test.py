from gvt_core import *

def test_regeneration():
    ''' Testing for adding health to the card
    '''
    #setup
    player = Player("Quizmaker")
    card = Card("Quizzmakkerrr", 4, "Trolls", regeneration)
    power = Power("Regeneration", "Adds 1 health to the card", regeneration)
    card.add_power(power)
    player.add_to_hand(card)
    
    health_init = card.get_health()
    #invoke
    card.take_damage(2, player)
    #print("Health damaged", card.get_health())
    power.activate(player, card)
    #print("Health now", card.get_health())
    #analyze
    assert health_init - 2 + 1 == card.get_health()
    assert True == power.get_used()

def test_first_aid():
    ''' Testing for adding 5 score to the player
    '''
    #setup
    player = Player("Quizmaker")
    card = Card("Quizzmakkerrr", 4, "Trolls", regeneration)
    power = Power("First Aid", "Adds 5 points to the player", first_aid, True)
    card.add_power(power)
    player.add_to_hand(card)
    
    score_init = player.get_score()
    #invoke
    power.activate(player, card)
    can_use_again = power.activate(player, card) # If the power can be activated again
    #analyze
    assert score_init + 5 == player.get_score()
    assert True == power.get_single_use()
    assert True == power.get_used()
    assert False == can_use_again

def test_card_activate():
    ''' Testing the card activate function
    '''
    #setup
    player = Player("Quizmaker")
    card = Card("Quizzmakkerrr", 4, "Trolls", regeneration)
    power = Power("First Aid", "Adds 5 points to the player", first_aid, True)
    card.add_power(power)
    player.add_to_hand(card)

    score_init = player.get_score()
    #invoke
    card.activate(player)
    #analyze
    assert score_init + 5 == player.get_score()

def test_battle():
    ''' Testing our battle function
    '''
    #setup
    random.seed(1000)
    player1 = Player("Guldan")
    player2 = Player("Thrall")
    card = Card("Murloc", 4, "Trolls", regeneration)
    card_dog = Card("The dog", 1, "Trolls", first_aid)
    power = Power("Regeneration", "Adds 1 health to the card", regeneration)
    power_score = Power("First Aid", "Adds 5 points to the player", first_aid, True)
    card.add_power(power)
    card_dog.add_power(power_score)

    player1.add_to_hand(card)
    player1.add_to_hand(card_dog)
    player2.add_to_hand(card_dog)
    #invoke
    player1.battle(0, player2, 0)
    #assert
    assert 6 == player2.get_hand()[0].get_health()

def test_add_to_discard():
    ''' Testing our add to discard function after
        a card reaches 0 health, in conjunction with
            the battle function
    '''
    #setup
    random.seed(1000)
    player1 = Player("Guldan")
    player2 = Player("Thrall")
    card = Card("Murloc", 4, "Trolls", regeneration)
    card_dog = Card("The dog", 1, "Trolls", first_aid)
    power = Power("Regeneration", "Adds 1 health to the card", regeneration)
    power_score = Power("First Aid", "Adds 5 points to the player", first_aid, True)
    card.add_power(power)
    card_dog.add_power(power_score)

    player1.add_to_hand(card)
    player1.add_to_hand(card_dog)
    player2.add_to_hand(card_dog)
    #invoke
    player2.get_hand()[0].take_damage(100, player2) # Forcefully killing the card
    #assert
    assert [] == player2.get_hand()

def test_cards_sort():
    ''' Testing if the cards are sorted by rarity and cost
    '''
    #setup
    random.seed(1)
    player1 = Player("Guldan")
    card1 = Card("Murloc", 1, "Trolls", regeneration)
    card2 = Card("Monster", 2, "Trolls", regeneration)
    card4 = Card("Boo", 4, "Trolls", regeneration)
    card5 = Card("Kisses", 2, "Trolls", regeneration)
    power = Power("Regeneration", "Adds 1 health to the card", regeneration)
    card1.add_power(power)
    card2.add_power(power)
    card4.add_power(power)
    card5.add_power(power)

    #invoke; automatically sorts the cards after appending it to the hand
    player1.add_to_hand(card1)
    player1.add_to_hand(card2)
    player1.add_to_hand(card4)
    player1.add_to_hand(card5)
    
    #assert
    card = player1.get_hand()
    # Card 1; should be rarity 1 and cost 1
    assert 1 == card[0].get_rarity()
    assert 1 == card[0].get_cost()
    # Card 2; should be rarity 2 and cost 4
    assert 2 == card[1].get_rarity()
    assert 4 == card[1].get_cost()
    # Card 3; should be rarity 2 and cost 5
    assert 2 == card[2].get_rarity()
    assert 5 == card[2].get_cost()
    # Card 4; should be rarity 4 and cost 10
    assert 4 == card[3].get_rarity()
    assert 10 == card[3].get_cost()

def main():
    '''Testing str and repr here from our class Card
    '''
    card = Card("Murloc", 3, "Trolls", regeneration)
    card_dog = Card("The dog", 2, "Trolls", regeneration)
    power = Power("Regeneration", "Adds 1 health to the card", regeneration)
    power_score = Power("First Aid", "Adds 5 points to the player", first_aid, True)

    card.add_power(power)
    card_dog.add_power(power_score)
    print("__str__", card, card_dog)
    print("\n__repr__")
    print(repr(card), repr(card_dog))
    pass
if __name__ == "__main__":
    #main()
    pass

"""
Test code for later
def activate(self, player): # Can pass in activate to check if it has a power, then the card activates at the start of each round
    '''Activates the power function if the card has a power
    Can be immediately ran at the start of the round if they have a power (assignment 12.1, problem 7a)        
    '''
    for hand in player.get_hand():
        if hand.get_name() == self.__name:
            if self.__power_func != None:
                self.__power_func.activate(player, self)
            else:
                print(self.__name, "does not have a power")
        else:
            print(player.get_name(), "does not have the card", self.__name, "in their hand!")

def regeneration(player, card):
    card.add_health(1)
    print(card.get_name(), "healed for 1 health!")
    return True
"""