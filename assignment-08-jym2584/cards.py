import random
def make_card(rank, suit): # Rank if it's special and number
    ''' This makes a card
    rank: Rank of a card from 2 to 14
    suit: Suit of a card from Hearts, Diamonds, Clubs, Spades

    shorthand_colored = takes shorthand and colorizes it based on the suit of a card
    
    returns:
    rank, suit, name (Name of hte card), shorthand (Abbreviation of the card)
    '''
    if rank < 2 or rank > 14:
        raise IndexError("Rank must be 2-14: " + str(rank))

    name = " of " + str(suit)
    shorthand = ""
    shorthand_colored = ""

    if rank <= 10:
        name = str(rank) + name
        shorthand = str(rank)
    elif rank == 11:
        name = "Jack" + name
        shorthand = "J"
    elif rank == 12:
        name = "Queen" + name
        shorthand = "Q"
    elif rank == 13:
        name = "King" + name
        shorthand = "K"
    elif rank == 14:
        name = "Ace" + name
        shorthand = "A"

    if suit == "Hearts":
        shorthand += "H"
        shorthand_colored = "\033[31m" + shorthand + "\033[37m"
    elif suit == "Diamonds":
        shorthand += "D"
        shorthand_colored = "\033[31m" + shorthand + "\033[37m"
    elif suit == "Clubs":
        shorthand += "C"
        shorthand_colored = "\033[34m" + shorthand + "\033[37m"
    elif suit == "Spades":
        shorthand += "S"
        shorthand_colored = "\033[34m" + shorthand + "\033[37m"
    else:
        raise ValueError("Not a valid suit")

    #print(shorthand_colored, end=" ")
    return (rank, suit, name, shorthand_colored)

def make_deck():
    '''Makes a deck of every card using 2 for loops
    i = based on rank
    j = based on suit
    '''
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    #deck_count = 52
    make_a_list = []
    for each_rank in range(2, 15): #Grabs card values from 2 to 14
        for each_suit in suit: #Grabs suit lists!
            make_a_list.append(make_card(each_rank, each_suit))
            #print(make_a_list)
    
    #print("THis should print ace of spades", (make_a_list[51])[3]) #usually assign to variable and then access the variable
    return make_a_list
    #print("This should print a single value from the list", make_a_list[10])

def shuffle(make_a_list):
    """Shuffles the cards
    """
    length = len(make_a_list)
    counter = 0
    for i in range(length):
        j = random.randint(0, length-1)
        temp = make_a_list[i]
        make_a_list[i] = make_a_list[j]
        make_a_list[j] = temp
        counter +=1
    #print("Shuffled", counter, "cards")
    for index in range(len(make_a_list)):
        make_a_list[index][3] # This grabs the value of the fourth index
        #print((make_a_list[index])[3], end=" ") # Test print
    return make_a_list

def draw(deck, hand=None):
    '''This draws the top card from a deck pile.
    deck: This uses the list from a deck
    hand: parameter set to none so we can take a card from the deck and put it into the hand

    returns
    hand: grabs the hand of the card that was taken from the deck
    '''
    if hand == None:
        hand = []
    drawn_card = None
    testing = False # If true, this prints out how many cards there are initially and how many cards there are now. For testing purposes
    ###########################################
    '''Counting how many cards there are intially
    '''
    if testing == True:
        count = 0
        print("\n")
        for i in range(len(deck)):
            count += 1
            print(deck[i][3], end=" ")
        print(" (There are",count,"cards)")
    ###########################################
    '''This is our meat of the code where we draw our card now
    '''
    if len(deck) == 0:
        return None
    else:
        drawn_card = deck.pop()
        hand.append(drawn_card)
        print(hand[0][3], " has been drawn.", sep="")

    ###########################################
    ''' Counting how many cards there are now
    '''
    if testing == True:
        count2 = 0
        for i in range(len(deck)):
            count2 += 1
            print(deck[i][3], end=" ")
        print(" (There are now",count2,"cards)")
    ###########################################
    return drawn_card

def deal(deck, number):

    testing = False
    ###########################################
    '''Counting how many cards there are intially
    '''
    if testing == True:
        count = 0
        print("\n")
        for i in range(len(deck)):
            count += 1
            print(deck[i][3], end=" ")
        print(" (There are",count,"cards)")
    ###########################################
    '''This is the meat of our code where we draw our hands now
    '''
    hand_1 = []
    hand_2 = []
    for i in range(number):
        draw_from_deck = draw(deck) # This is for the first hand
        draw_from_deck2 = draw(deck) # This is for the second hand

        hand_1.append(draw_from_deck)
        hand_2.append(draw_from_deck2)
    if testing == True:
        print("\nHand 1:")
        for i in range(number):
            print(hand_1[i][3],end =" ")
        print("\nHand 2:")
        for i in range(number):
            print(hand_2[i][3], end= " ")

    ###########################################
    ''' Counting how many cards there are now
    '''
    if testing == True:
        count2 = 0
        print("\n")
        for i in range(len(deck)):
            count2 += 1
            print(deck[i][3], end=" ")
        print(" (There are now",count2,"cards on the deck)")
    ###########################################

    return hand_1, hand_2

def cut(deck):
    ''' Returns deck_half1, deck_half2
    '''
    if len(deck) == 0 or len(deck) == 1:
        raise ValueError("Cannot cut a deck with 0 or 1")
    half_length = len(deck)//2
    #print(half_length)
    deck_half1 = []
    deck_half2 = []

    deck_half1.append(deck[:half_length])
    deck_half2.append(deck[half_length:])

    print("Deck 1")
    for i in range(half_length):
        print(deck_half1[0][i][3], end=" ")
    
    print("\nDeck 2")
    for i in range(half_length):
        print(deck_half2[0][i][3], end=" ")

    return deck_half1, deck_half2

def main():
    deck = make_deck()
    cut(deck)
    #print(make_card(10,"Hearts"))
    #print(make_card(14,"Spades"))
    #make_card(10,"Hearts")
    #make_card(14,"Spades")
    #make_deck()
    #shuffle(make_deck())

    #deck = shuffle(make_deck())
    #draw(deck)

    #print("\nDeal function start\n------------------------------------------------------------")
    #deck_with_num = card_number(deck, 4)
    #deal(deck, 8)
    #print("\nDeal function end\n------------------------------------------------------------")
    #suit()
    #cut(deck_with_num)

if __name__ == "__main__":
    main()


def suit():
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    for i in range(len(suit)):
        print(i, suit[i])