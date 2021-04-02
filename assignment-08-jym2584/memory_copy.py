def make_board(rows, cols):
    ''' Fri, Oct 9 BROKEN CODE

    Issues:
    Card isn't shuffled after making the deck flippable
    selected + selected repeats.
        Eg) [1,2,3] [1,2,3] ---> [1,2,3,1,2,3]
                                If I set index 0 to True, index 3 will also be true. This should not happen....
                                Crosspost: https://discordapp.com/channels/744553631054954636/762749289582690335/764296919912415242
    '''
    testing = True
    deck = cards.make_deck()
    cards.shuffle(deck) ########## I need to shuffle the deck after making it flippable (Fri, Oct 9) ##########
    
    flippable = []
    for i in range(len(deck)):
        flippable.append(make_flippable(deck[i])) 
        
    selected = select_card(rows * cols, flippable) ########## Probably need to do something with this as well. Maybe shuffle after duplicating the cards? (Fri, Oct 9) ##########
    board = [[] for _ in range(rows)]
    for row in board:
        for col in range(cols):
            row += [selected.pop()]
    
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









def make_board(rows, cols, deck):
    ''' Fri, Oct 9 BROKEN CODE

    Issues:
    Card isn't shuffled after making the deck flippable
    selected + selected repeats.
        Eg) [1,2,3] [1,2,3] ---> [1,2,3,1,2,3]
                                If I set index 0 to True, index 3 will also be true. This should not happen....
                                Crosspost: https://discordapp.com/channels/744553631054954636/762749289582690335/764296919912415242
    '''
    testing = False
    #deck = cards.make_deck()
    cards.shuffle(deck) ########## I need to shuffle the deck after making it flippable (Fri, Oct 9) ##########
    
    flippable = []
    for i in range(len(deck)):
        flippable.append(make_flippable(deck[i])) 
        print("FLIPP",flippable[i])
    selected = select_card(rows * cols, flippable) ########## Probably need to do something with this as well. Maybe shuffle after duplicating the cards? (Fri, Oct 9) ##########
    board = [_ for _ in range(rows)]
    for row in board:
        for col in range(cols):
            row += [selected.pop()]
    
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