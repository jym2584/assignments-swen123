class Card:
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = str(rank) + " of " + suit
        self.shorthand = str(rank) + suit[0]

a_card = Card (5, "Hearts")
print(a_card.name)