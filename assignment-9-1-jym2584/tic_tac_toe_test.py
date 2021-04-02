from tic_tac_toe import *
import io

def test_make_board():
    '''Tests making the board
    @param board, makes the board via list
    @param actual, prints the actual board
    '''
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    actual = make_board()
    assert board == actual

def convert_to_board(board_string):
    ''' Converts string into a board
    @param board, makes an empty list
    @param rows, splits the board_string by new lists

    @return board, returns board_string into a list
    '''
    board = []
    rows = board_string.split("\n")
    for i in range(0, len(rows), 2):
        board.append(rows[i].split("|"))
    return board


def test_convert_to_board(capsys):
    '''Captures the printed result of convert_to_board(board_str)
    and compares it with the expected.

    @param captured, captures what the function would print from the command terminal
    '''
    #Setup
    board_str = " |O| \n-----\nX|O| \n-----\n |X| \n"
    expected = "[[' ', 'O', ' '], ['X', 'O', ' '], [' ', 'X', ' ']]"
    
    #Invoke
    print(convert_to_board(board_str))
    #Analysis
    captured = capsys.readouterr().out
    assert expected == captured.strip()

def test_print_board(capsys):
    ''' Tests printing out a full board!
    @param board_string, prints out the string-ified version of the board.
    @param captured, captures the printed result of print_board from the command terminal

    asserting that the board_string is equal to the one that is pasted on the command terminal
    '''
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board_string = " | | \n-----\n | | \n-----\n | | \n"
    #Invoke
    print_board(board)
    #Analyze
    captured = capsys.readouterr().out
    assert board_string == captured

def test_make_move_valid(capsys, monkeypatch):
    ''' Tests the results of making the move!
    @param board, sets up an existing play
    @param expected, a move should be played
    @param symbol, used for running make_move
    @param captured_out, captures the make_move function

    assert, compares expected with the played board encased in convert_to_board
    '''
    #Setup
    board = [['X', ' ', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    expected = [['X', 'X', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    symbol = 'X'
    user_input = io.StringIO('0 1\n')
    monkeypatch.setattr('sys.stdin', user_input)

    #Invoke
    make_move(board, symbol)

    #Analyze
    captured_out = capsys.readouterr().out
    assert expected == convert_to_board(captured_out.split(": ")[-1])

def test_make_move_used(capsys, monkeypatch):
    ''' Asserts used results of making the move!
    
    asserts that the expected is equal to the first index of the newline split, which prints out the expected.
    '''
    #Setup
    board = [['X', ' ', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    expected = "Enter move (row col): Invalid move. Please try again."
    symbol = 'X'
    user_input = io.StringIO('0 0\n0 1\n')
    monkeypatch.setattr('sys.stdin', user_input)

    #Invoke
    make_move(board, symbol)

    #Analyze
    captured_out = capsys.readouterr().out
    assert expected == captured_out.split("\n")[0]

def test_make_move_invalid(capsys, monkeypatch):
    ''' Asserts invalid results of making the move!
    
    asserts that the expected is equal to the first index of the newline split, which prints out the expected.
    '''
    #Setup
    board = [['X', ' ', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    expected = "Enter move (row col): Invalid move. Please try again."
    symbol = 'X'
    user_input = io.StringIO('BROOOOOOOOOO INVALIDMOVE_YO....I_hope_I_did_this_right\n0 1\n') # Hope I did this right. Might refactor so that it only takes
    monkeypatch.setattr('sys.stdin', user_input)                                            # "Invalid move. Please try again.""

    #Invoke
    make_move(board, symbol)

    #Analyze
    captured_out = capsys.readouterr().out
    assert expected == captured_out.split("\n")[0]

def test_main_function(capsys, monkeypatch):
    ''' Tests the main game
    @param user_input, plays the entire game
    @param captured_out, returns printed stuff from user input

    captured_out.strip().split("\n")[-1], splits the captured output, splits it into newlines and grabs the last index which should be our expected.
    '''
    #Setup
    user_input = io.StringIO("0 0\n0 1\n 0 2\n1 0\n1 1\n 1 2\n2 0\n2 1\n 2 2")
    monkeypatch.setattr('sys.stdin', user_input)
    expected = "Game over!"
    #Invoke
    main()
    #Analyze
    captured_out = capsys.readouterr().out
    assert expected == captured_out.strip().split("\n")[-1]