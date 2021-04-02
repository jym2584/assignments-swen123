'''
Jin Moon

You are not allowed to add any additional functions to the code, use the ones
provided. Use python exam_test.py to run your code. If you must, you can add
calls into the section after if __name__ == "__main__" at the bottom of the file.

Practicum Question #5

The dot product of a matrix involves summing the product of the first matrix's 
rows by the second matrix's columns. The code for this is a little involved and
is provided for you.

You need to implement all the necessary rules required to perform the calculation. 
This includes:
    1. Determine the number of rows in matrix a
    2. Determine the number of columns in matrix b
    3. If they are not equal, raise an ValueError with an appropraite message
    4. If they are both size 0, return an empty list
    5. Determine the number of columns in matrix a
    6. Determine the number of rows in matrix b

Each matrix is encoded as a two dimensional list in [row][column] order.
Example: [[1, 2, 3]] is a matrix with one row and 3 columns
         [[4], [5], [6]] is a matrix with 3 rows and 1 column
         [[1, 2], [3, 4], [5, 6]] is a matrix with 3 rows and two columns
'''

def dot_product (matrix_a, matrix_b):

    rows_a = len(matrix_a)
    print("Rows A", rows_a)

    rows_b = len(matrix_b)
    print("ROWS B", rows_b)

    for i in matrix_a: # Finding columns in A
        columnsa = len(i)

    for i in matrix_b: # Finding columns in B
        columnsb = len(i)

    columns_a = columnsa
    print("Columns A",columns_a)

    columns_b = columnsb
    print("Columns B",columns_b)


    if rows_a == rows_b:
        raise ValueError("The rows are the same.")
    elif rows_a == None or rows_b == None:
        raise ValueError("Rows and/or Columns are empty.")
    ############ Provided Code - DO NOT MODIFY ############
    result = []
    for i in range (rows_a):
        row = []
        for k in range (columns_b):
            sum = 0
            for j in range (columns_a):
                sum += matrix_a[i][j] * matrix_b[j][k]
            row.append (sum)
        result.append (row)

    return result
    ############ End Provided Code ############


if __name__ == "__main__":
    '''Use python exam_test.py to test your code.
       If you must add your own test code here. '''
    matrix_a = [[1, 2, 3]]
    matrix_b = [[4], [5], [6]]
    print(dot_product(matrix_a, matrix_b))