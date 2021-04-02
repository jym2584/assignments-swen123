"""
Python implementations of common search algorithms.

@author GCCIS Faculty
"""

import arrays
import array_utils

def linear_search(an_array, target):
    """
    Searches an array for a target value.
    """
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None

def increasing_comparator(a,b):
    return a < b

def decreasing_comparator(a,b):
    return a > b


def binary_search(an_array, target, comparator=increasing_comparator, start=None, end=None):
    """
    An implementation of the binary search algorithm.
    """
    if start == None:
        start = 0
    if end == None:
        end = len(an_array) - 1

    if start > end:
        return None
    else:
        mid = (start + end) // 2
        value = an_array[mid]
        if value == target:
            return mid
        elif comparator(value,target):
            start = mid + 1
            return binary_search(an_array, target, comparator, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, comparator, start, end)

def print_first(comparator, a, b):
    if comparator(a,b): # if true, a is first
        print(a,b)
    else: # b is first
        print(b,a)

def more_than(a,b):
    return a >= b


def main():
    #print_first(more_than,5,10)
    an_array = array_utils.range_array(100,0,-1)
    print(binary_search(an_array, 75, decreasing_comparator))
main()