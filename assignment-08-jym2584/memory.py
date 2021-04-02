import cards
import time
import random

testing = False

def make_flippable(card):
    return [False, card]

def ismatch(card1, card2):
    if card1[0] and card2[0]: # If 2 cards are face up
        print("Both cards are faceup")
        if card1[1][2] == card2[1][2]: # If they are also equal. This accesses the card name inside of the make_flippable list
            print("Both cards are equal")
            return True
        else:
            print("Both cards are not equal") 
            return False
    else:
        print("Both cards are facedown")
        return False

def select_card(number, deck):
    if number == 0 or number < 0:
        raise ValueError("You can't select an empty number of cards")
    elif number % 2 != 0:
        raise ValueError("The number needs to be even!")
    elif number > len(deck):
        raise ValueError("The number can't be more than the deck!")
    else:
        half = number // 2
        selected = deck[:half]
        dupe_cards = selected + selected ########## Probably need to do something with this. (Fri, Oct 9) ##########

        #print("Cards")
        #for i in range(0, len(dupe_cards)):
            #print(dupe_cards[i][3], end = " ")
        return dupe_cards


def make_board(rows, cols, deck):
    ''' Fri, Oct 9 BROKEN CODE

    Issues:
    Card isn't shuffled after making the deck flippable
    selected + selected repeats.
        Eg) [1,2,3] [1,2,3] ---> [1,2,3,1,2,3]
                                If I set index 0 to True, index 3 will also be true. This should not happen....
                                Crosspost: https://discordapp.com/channels/744553631054954636/762749289582690335/764296919912415242
    '''
    #deck = cards.make_deck()
    cards.shuffle(deck) ########## I need to shuffle the deck after making it flippable (Fri, Oct 9) ##########
    
    flippable = []

    #for i in range(len(deck)):
        #flippable.append(make_flippable(deck[i])) 
    
    selected = select_card(rows * cols, deck) ########## Probably need to do something with this as well. Maybe shuffle after duplicating the cards? (Fri, Oct 9) ##########
    # Shuffle card
    # selectable
    # flippable

    for i in range(len(selected)):
        flippable.append(make_flippable(selected[i])) 


    board = [[] for _ in range(rows)]
    for row in board:
        for col in range(cols):
            row += [flippable.pop()]
    #print(board)
    ###################################################################################
    ''' Tests before
    '''
    #print(board)
    #Prints out the board
    if testing == True:
        for row in range(rows):
            print("\n")
            for column in range(cols):
                print([board][0][row][column][0], end=" ")

        for row in range(rows):
            print("\n")
            for column in range(cols):
                print([board][0][row][column][1][3], end=" ")

        print("\nRows:", rows, "| Columns:", cols)
        ####################################################################################
        '''Where we want to manually test

            board[row][column][truefalse(0) or card(1)][if card then 0-3 to access card ]
        '''
        print("------------OUR TEST-----------------")
        print("Setting row 0 column 0 to true")
        board[0][0][0] = True
        print("Setting row 2 column 2 to true")
        board[2][2][0] = True
        print("--------------------------------------")
        ####################################################################################
        '''Testing after
        '''
        for row in range(rows):
            print("\n")
            for column in range(cols):
                print([board][0][row][column][0], end=" ")

        for row in range(rows):
            print("\n")
            for column in range(cols):
                print([board][0][row][column][1][3], end=" ")

        print("\nRows:", rows, "| Columns:", cols)
        ####################################################################################
    return board

def print_board(board):
    for row in board:
        print()
        for flippable in row:
            #CHeck to see if the flipable is none
            if flippable[1] == None:
                print("    ", end="")
            elif flippable[0]:
                card = flippable[1]
                print(card[3], end=" ")
            else:
                print("[-] ", end="")
            #print()

def make_move(board):
    no_quit = True
    while no_quit == True:
        try:
            askmove = input("\nMake move (row, column): ")
            tokens = askmove.split(" ")
            row = int(tokens[0])
            column = int(tokens[1])
            #print("Row", row)
            #print("Column", column)
            no_quit = False
            return row, column
        except ValueError:
            print("Not a valid integer")
        except IndexError:
            print("You need a column")

def is_digit():
    no_quit = True
    while no_quit:
        row = (input("Enter a row: "))
        column = (input("Enter a column: "))

        if row.isdigit() == False or column.isdigit() == False:
            raise ValueError("Inputs must be numbers!")
        else:
            print("Passed")
            no_quit = False
            return row, column
    
def flip(row,column, board):
    try:
        board[row][column][0] = True
    except IndexError:
        print("Not a valid integer")
    except IndexError:
        print("Invalid input. (row, column)")

def main():
    ''' Test function
    '''
    deck = cards.make_deck()
    board = make_board(2,2, deck)
    print("Flippable list", board[1][1])
    print("Card printing", board[1][1][1])
    board[1][1][1] = None
    print("Flippable list w/ board set to None", board[1][1])

def the_game():
    #Initializes the deck
    deck = cards.make_deck()
    rowinput =str(input("Enter row: "))
    columninput = str(input("Enter column: "))
    
    # Checks if the row is a digit
    if rowinput.isdigit() and columninput.isdigit():
        pass
    else:
        print("not is a digit. Quitting...")
        quit()
    
    # Makes the board
    board = make_board(int(columninput), int(rowinput), deck)
    print_board(board)

    ####### Meat of the code; the game #########
    score = 0
    is_finished = False

    while is_finished == False: # While the game hasn't finished
        try:
            if score == (int(columninput) * int(rowinput))//2: # The player wins if they reach the score that is equal to half the inputted row/column
                print("\nYou win!")                             # Other words, they win if all the cards matches
                is_finished = True
            else:
                start = time.time() # Calculates the time it takes to perform the first 2 moves
                row, column = make_move(board) # Prompt for the first input
                flip(row, column, board) # Make their input true
                print_board(board) # Prints the board

                row2, column2 = make_move(board) # Asks for the second input
                flip(row2, column2, board)
                end = time.time()
                print_board(board)

                if row2 == row and column == column2: # Mismatch error checking. If the player moves on the same position twice.
                    print("You can't match a card of the same position.")
                    board[row][column][0] = False
                    board[row2][column2][0] = False

                elif board[row][column][1] == None and board[row2][column2][1] == None: # Mismatch error checking. If the player is matching a card with nothing (vice versa) or both. 
                    print("\nYou're... matching nothing?")

                elif board[row][column][1][2] != board[row2][column2][1][2]: # Mismatch error checking. If the cards are not matching
                    print("Not a match")
                    print("\nScore:",score)
                    board[row][column][0] = False
                    board[row2][column2][0] = False
                else:
                    #print("Is match!") # If the card names of both inputs are true, lets pass in true
                    score += 1
                    print("\nScore:",score)
                    print("Time: ", round(end-start, 1), "seconds")
                    board[row][column][1] = None
                    board[row2][column2][1] = None

        except IndexError:
            print("Not a valid move. Try again.")
            if board[row][column][1][2] == True:
                board[row][column][1][2] = False
            elif board[row2][column2][0] == True:
                board[row2][column2][0] == False
            else:
                pass
        except ValueError:
            print("Not a valid move. Try again.")
            if board[row][column][1][2] == True:
                board[row][column][1][2] = False
            elif board[row2][column2][0] == True:
                board[row2][column2][0] == False
            else:
                pass
        print_board(board)

    

if __name__ == "__main__":
    #main()
    the_game()