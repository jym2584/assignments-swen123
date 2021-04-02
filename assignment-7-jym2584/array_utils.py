"""
Various utilities for creating and manipulating arrays.

@author GCCIS Faculty
"""

import arrays
import random

def range_array(start, stop, step=1):
    """
    Creates and returns an array from the specified range.
    """
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def random_array(size, min_value=0, max_value=None):
    """
    Creates an array of the specified size with random values ranging from 
    min_value to max_value. Values may be repeated.
    """
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def is_sorted(an_array):
    """
    Returns True if the array is sorted in increasing order, and False 
    otherwise.
    """
    length = len(an_array)
    if length <= 1:
        return True

    for index in range(1, len(an_array)):
        if an_array[index] < an_array[index-1]:
            return False
    return True

def shuffle(an_array):
    """
    Shuffles the elements in the array into a random order.
    """
    length = len(an_array)
    for i in range(length):
        j = random.randint(0, length-1)
        temp = an_array[i]
        an_array[i] = an_array[j]
        an_array[j] = temp
####################################################################
def create_array(filename):
    '''Creates an array given the filename
    '''
    with open(filename) as file:
        length = int(next(file))
                    #arrays.Array(length, prototype)
        an_array = arrays.Array(length)
        index = 0
        for line in file:
            value = int(line)
            an_array[index] = value
            index += 1
    return an_array

def copy_array(an_array, length=None):
    '''Copies an array given an array
    '''
    if length == None:
        length = len(an_array)
    copy = arrays.Array(length)
    for i in range(length):
        copy[i] = an_array[i]
    return copy

####################################################################

def main():
    #array = create_array("data/random.txt")
    #print(array)
    #print(copy_array(array))
    
    #print(cat(arrays.Array(1,2), arrays.Array(1,3)))
    pass

if __name__ == "__main__":
    main()