"""
The dot product of a matrix involves summing the product of the first matrix's rows by the 
second matrix's columns. 

Each matrix is encoded as a two dimensional list in [row][column] order.
Example: [[1, 2, 3]] is a matrix with one row and 3 columns
         [[4], [5], [6]] is a matrix with 3 rows and 1 column
         [[1, 2], [3, 4], [5, 6]] is a matrix with 3 rows and two columns
"""
def dot_product (matrix_a, matrix_b):
    rows_a = len (matrix_a)
    columns_b = len (matrix_b)
    if columns_b != 0:
        columns_b = len(matrix_b[0])

    if rows_a != columns_b:
        raise ValueError ("Matrices are not correctly sized")

    if rows_a == 0 and columns_b == 0:
        return []

    columns_a = len (matrix_a[0])
    rows_b = len (matrix_b)
    
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
                        
if __name__ == "__main__":
    '''
    Psuedo test just in case you cannot run the debugger in test mode.
    '''

    matrix_a = [[1, 2, 3]]
    matrix_b = [[4], [5], [6]]
    expected_a_dot_b = [[32]]
    expected_b_dot_a = [[4, 8, 12], [5, 10, 15], [6, 12, 18]]

    actual_ab = dot_product (matrix_a, matrix_b)
    actual_ba = dot_product (matrix_b, matrix_a)

    print (actual_ab)
    print (actual_ba)