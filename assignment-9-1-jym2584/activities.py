def factorial (num):
    if num < 0:
        raise ValueError ("Number must be 0 or greater")
    elif num == 0:
        return 1
    else:
        return num * factorial (num - 1)

def is_equally_divisable(numerator, denominator):
    if numerator % denominator == 0:
        print(numerator, "Is equally divisble to", denominator)
    else:
        print(numerator, "Is not equally divisble to", denominator)

def get_move():
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    symbol = input("Enter symbol (X or O): ")

    return row, column, symbol