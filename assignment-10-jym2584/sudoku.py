"""The sudoku game
"""
import pathlib
def create_sudoku_board(filename):
    ''' Creates the sudoku board as a list
    @param board, list that will contain digits in each row
    @param row, adds digits to a row
    @param digit, converts each number string into an integer

    @return board, returns the list that contains a 3x3
    '''
    try:
        with open("data/"+filename+".sud") as file:
            board = []
            row = []
            for line in file:
                line = line.strip()
                row = []
                for each_digit in line:
                    if each_digit.isdigit():
                        digit = int(each_digit)
                        #row.append(digit)
                    else:
                        pass
                    row.append(digit)
                board.append(row)
            return board
    except:
        return None

def format_board(row = -1, column = -1, board = "invalid_001"):
    ''' Formats the board into a pretty print thing
    @param board, creates the 2d list from create_sudoku_board
    @param row_counter and column_counter, adds a new line every 3 rows/columns

    ####@return board, returns the pretty print thing
    '''
    #board = create_sudoku_board(board)
    row_counter = 0
    column_counter = 0
    #print(len(board))
    
    for rows in range(len(board)):
        print() # breaks every list into a new line
        if row_counter % 3 == 0: # Let's add a new line every 3 rows
            print()
        row_counter += 1

        for col in range(len(board)):
            if column_counter % 3 == 0:
                print("", sep="", end=" ") # Let's add a new line every 3 columns
            column_counter += 1

            is_duplicate = find_duplicate(row, column, board)

            if is_duplicate: # If a duplicate is found, replace the value's text color to reflect a duplicate.
                value = board[row][column]
                board[row][column] = "\033[31m" + str(value) + "\033[37m" ### Should probably put this on find_duplicate instead.

            print("[",board[rows][col],"]", sep="", end= "") # does the pretty print thing (prints the numbers in brackets)
            #print("\033[31m[",board[1][1],"]\033[37m", sep="", end= "") # does the pretty print thing (prints the numbers in brackets)
    
    
            #is_duplicate = find_duplicate(row, column, board)

            #if not is_duplicate or row == -1 or column == -1:
                #print("[",board[rows][col],"]", sep="", end= "") # does the pretty print thing (prints the numbers in brackets)
            #else:
                #print("\033[31m[",board[rows][col],"]\033[37m", sep="", end= "") # does the pretty print thing (prints the numbers in brackets)    
    
    
    
    
    
    
    
    
    #print()
    #print(board[0][1])
    #return board # returns the pretty print thing




def find_duplicate(row, column, board = "invalid_001"):
    ''' Finds if there is a duplicate at a given row and column
    '''
    #board = create_sudoku_board(board)
    col_list = []
    # for i in board
    # for j in lenboard
    # if board = col_list

    #Test code
    #print("Length of board", len(board))
    #print("Row List", board[row]) # row at index 2
    
    for i in range(len(board)): # Grabs a column and inserts it into a list
        col_list.append(board[i][column]) # column at index 2
    #print("Column List", col_list)

    find_duplicate_list = [] # List for grabbing potential duplicates

    # Finding matching value by searching the column and row
    for i in range(len(board)-1): # For each row in the board
        for j in range(len(col_list)-1): # And for each column in the list
            if board[0][i] == col_list[j]: # If there is a value at a specified row and column that are the same
                #print("Found matching value:", col_list[j])
                find_duplicate_list.append(col_list[j]) # Append it to the list
    
    #Treat each section like it's own little board
    #Iterate through a section on the board as an individual board
    #Helper function on each section, create a set of 9 values
    # Figure out how to convert each section into a set

    if len(find_duplicate_list) == len(set(find_duplicate_list)): # If the length of the list is the same as the set of the list
        #print("There are no duplicates!")  # There are no duplicates!
        return False
    else: # However, if the set of the list is less than the length of the list
        #print("There are duplicates at row", row, "column", column) # A duplicate exists.
        return True

def validate_puzzle(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    for row in range(9):
        for col in range(9):
            row_set = rows[row]
            col_set = cols[col]
            move = board[row][col]
            if move in row_set or move in col_set:
                board[row][col] = "\033[31m" + str(move) + "\033[37m" ### Should probably put this on find_duplicate instead.
                format_board(row, col, board)
                return False
            else:
                row_set.add(move)
                col_set.add(move)
    return True

def validate_the_puzzles():
    for i in range(1,7):
        validate_puzzle(create_sudoku_board("invalid_00"+str(i)))
        print("\nPuzzle at invalid_00"+str(i),"invalid!")

    for j in range(1,11):
        if j < 10:
            validate_puzzle(create_sudoku_board("valid_00"+str(j)))
        else:
            validate_puzzle(create_sudoku_board("valid_010"))
    print("Puzzle valid from valid_001 to valid_010")


def main():
    #print(create_sudoku_board("invalid_001"))
    #the_board = create_sudoku_board("invalid_001")
    #print_board(2,2)
    #print("Is valid?", validate_puzzle(board))
    validate_the_puzzles()
    #format_board(3, 6, "invalid_001")
    #find_duplicate(3, 6)
    pass
main()