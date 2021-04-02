import array_utils as a
import arrays
import random
from testing import *
import sorts

def test_create_array():
    #setup
    filename = "data/random.txt"
    filename2 = "data/random2.txt" # This contains the arrays [1,3,5,6,9]
    #invoke
    new_array = a.create_array(filename)
    new_array2 = a.create_array(filename2)
    sorts.insertion_sort(new_array)
    #analyze
    assert_equals("Arrays", "[1, 3, 5, 6, 9]", str(new_array2))
    #print(new_array)
    assert_equals("Array", 0, new_array[0]) # These tests random.txt as indicated by the assignment.
    assert_equals("Array", 1, new_array[1]) # However the arrays on this file after sorting it is [0,1,2,12,16]
    assert_equals("Array", 2, new_array[2])
    assert_equals("Array", 12, new_array[3])
    assert_equals("Array", 16, new_array[4])

def run_all_tests():
    run_test(test_create_array)

run_all_tests()