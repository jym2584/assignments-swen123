import cards
import activities

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

def hand_score(hand):
    ''' Calculates score
    If rank is less than 10, prints the rank as score
    If rank is more than 10, prints the rank as 10
    '''
    score = 0
    for card in hand:
        rank = card[0]
        if rank <= 10:
            score+= rank
        elif rank < 14:
            score+= 10
        else: # Else if the hand is an ace
            if score + 11 < 21: #If the score is more than 10, add the score as 11
                score+= 11
            else: score += 1 # Otherwise it prints the score as 1
    return score

def print_hand_and_score(name, hand):
    '''Prints the name, hand and score
    Uses for loop to get the shorthand color of the hand
    Also calculates score
    '''
    score = hand_score(hand)
    print("\nPlayer:",name)
    for card in hand:
        print(card)
        print(card[3], end = " ")
    if score > 21:
        print("Score -", score, "(busted)")
    else:
        print("Score -",score)
    return score

def win_lose_or_draw(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        print("\nGame ends in a draw")
    elif player_score == dealer_score:
        print("\nGame ends in a draw")
    elif player_score > 21:
        print("\nDealer wins")
    elif dealer_score > 21:
        print("\nYou win!")
    elif dealer_score > player_score:
        print("\nDealer wins")
    else:
        print("\nYou win!")

def dealer_hit_or_stand(player_score, dealer_score):
    hit2 = None
    if player_score > 21:
        print("\n>> Dealer stands")
        hit2 = False
        return hit2
    elif dealer_score < 17 or dealer_score < player_score:
        print("\n>> Dealer hits")
        hit2 = True
        return hit2
    else:
        print("\n>> Dealer stands")
        hit2 = False
        return hit2

def player_hit_or_stand():
    no_quit = True
    hit = None
    prompt = input("Hit (h) or stand (s)?")
    while no_quit:
        if prompt == "h":
            print("\n>> You hit")
            no_quit = False
            hit = True
            return hit
        elif prompt =="s":
            print("\n>> You stand")
            no_quit = False
            hit = False
            return hit
        else:
            prompt = input("Hit (h) or stand (s)?")
            no_quit=True


def main():
    #Entering the person's name
    name = input("Enter your name: ")
    
    #We make the deck!
    deck = cards.shuffle(cards.make_deck())
    #deck_half1, deck_half2 = cards.cut(deck)
    #print("\n")
    hand1, hand2 = cards.deal(deck, 2)

    # Sorts the hands
    hand1.sort(key=suit_key)
    hand2.sort(key=suit_key)
    #Prints out the name
    player_score = print_hand_and_score(name, hand1)
    dealer_score = print_hand_and_score("Dealer", hand2)

    #Prompts the player to hit or stand
    hit = player_hit_or_stand()

    ## If the player hits, draw a card
    if hit:
        print("You draw a card.")
        hand1.append(cards.draw(deck))

    #Display their score
    player_score = print_hand_and_score(name, hand1)
    
    # Dealer hits or stands
    hit2 = dealer_hit_or_stand(player_score,dealer_score)

    #IF the dealer hits, draw a card
    if hit2:
        print("Dealer draws a card.")
        hand2.append(cards.draw(deck))

    #Display their score
    dealer_score = print_hand_and_score("Dealer", hand2)

    #Round end
    win_lose_or_draw(player_score, dealer_score)


    #If true, the dealer hits or stands
    #if player_hit_or_stand is True:
        #print("True")
        #dealer_hit_or_stand(player_score, dealer_score)







def main2():
    ###### Additional test for hand_score
    deck = cards.shuffle(cards.make_deck())
    hand1, hand2 = cards.deal(deck, 2)
    #print("Hand 1 score:",hand_score(hand1))
    #print("Hand 2 score:",hand_score(hand2))

    # Test for print_hand_and_score
    print("Print hand and score\n----------------------------------")
    print_hand_and_score("Buttercups", hand1)
    # Test for win lose or draw


if __name__ == "__main__":
    main()
    #main2()