def make_board():
    return[[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for j in range (len(board)-1):
        for i in range (len(board[j]) - 1):
            print(board[j][i], end='|')
        print (board[j][-1])
        for i in range (len(board[j]) - 1):
            print('-', end= '-')
        print('-')
    for i in range (len(board[-1]) -1):
        print(board[-1][i], end='|')
    print()


def make_move(board,row,column,move):
    board[row][column] = move

def main():
    board = make_board()
    print_board(board)
    while True:
        move = input("Enter a move (row, column, X or 0): ")
        if move == '':
            break
        move = move.split(',')
        make_move(board, int(move[0]), int(move[1]), move[2])
        print_board(board)
main()