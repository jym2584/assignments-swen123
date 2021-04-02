'''
Jin Moon

You are not allowed to add any additional functions to the code, use the ones
provided. Use python exam_test.py to run your code. If you must, you can add
calls into the section after if __name__ == "__main__" at the bottom of the file.

Practicum Question #3

Implement the function named "reverse_array" that has a parameter for 
"an_array." The function should reverse the order of the elements in
the array IN PLACE. That is to say that you should not copy the
array, but should modify the elements within the array.

Be sure to handle specific edge cases like empty arrays or arrays
with only one element.
'''

import arrays
import array_utils

def reverse_an_array(an_array):
    if an_array == None or len(an_array) == 0:
        raise ValueError("There's no array to reverse.")
    elif len(an_array) == 1:
        raise ValueError("There is only 1 array. There's no array to reverse")
    else:
        length = len(an_array)
        for i in range(len(an_array)):
            an_array[i] = length-i
        return an_array

if __name__ == "__main__":
    an_array = array_utils.range_array(0,10)
    an_array2 = array_utils.range_array(0,0)
    print(an_array)
    print(reverse_an_array(an_array))
