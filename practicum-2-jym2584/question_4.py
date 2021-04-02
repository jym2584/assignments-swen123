'''
Jin Moon

You are not allowed to add any additional functions to the code, use the ones
provided. Use python exam_test.py to run your code. If you must, you can add
calls into the section after if __name__ == "__main__" at the bottom of the file.

Practicum Question #5

Implement the *recursive* function, bin_to_int, that takes at least one parameter - an array
representing a binary number.  The array will contain only 0 or 1 integers.

A binary number is converted to an integer by working right to left.  The right-most value
is multiplied by 2^0.  The second right-most value is multiplied by 2^1, and so on.  The
result of these individual operations are summed together to get the integer equivalent.

Example:
1101 = 15

b[0] = 1 * 2^3 = 8
b[1] = 1 * 2^2 = 4
b[2] = 0 * 2^1 = 0
b[3] = 1 * 2^0 = 1

8 + 4 + 0 + 1 = 13
'''

import arrays

def bin_to_int (an_array, index = 0):
    a_list = []
    for i in an_array:
        a_list.append(an_array[i])
    
    if index <= 0:
        return bin_to_int(an_array, index)
    for i in an_array:
        print(i)
    return bin_to_int(an_array, index+1)


if __name__ == "__main__":
    '''Use python exam_test.py to test your code.
        If you must add your own test code here. '''
    an_array = "1101"
    bin_to_int(an_array)