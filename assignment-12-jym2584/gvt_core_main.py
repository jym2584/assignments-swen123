from gvt_core import *

player1 = Player("Guldan")
player2 = Player("Thrall")
card = Card("Murloc", 3, "Trolls", regeneration)
card_dog = Card("The dog", 2, "Trolls", regeneration)
power = Power("Regeneration", "Adds 1 health to the card", regeneration)
power_score = Power("First Aid", "Adds 5 points to the player", first_aid, True)

card.add_power(power)
card_dog.add_power(power_score)

player1.add_to_hand(card)
player1.add_to_hand(card_dog)
player2.add_to_hand(card_dog)
print(card, card_dog)
repr(card)

print(player1.get_name(),"(player) current hand:")
for cards in player1.get_hand():
    print("   ",cards.get_name(), "Health:",cards.get_health())
    print("    ", end = "")
    #cards.print_card()
    print("\n")

#card.take_damage(5, player1)
print("Health", card.get_health())
card.activate(player1)
print("Health now", card.get_health())

player1.battle(0, player2, 0)