import arrays
import random
import time
import array_utils as a
from testing import *

def test_range_array():
    new_array = a.range_array(0,1)
    assert_equals("new array", 0, new_array[0])

    another_array = a.range_array(5,6)
    assert_equals("another array", 5, another_array[0])

def test_range_arrays():
    new_array = a.range_array(0,5,2)
    range_array = range(0,5,2)
    for i in range(0, len(new_array)):
        assert_equals("range array", range_array[i], new_array[i])
        #assert_equals("3 ranges 0", 0, new_array[0])
        #assert_equals("3 ranges 1", 2, new_array[1])
        #assert_equals("3 ranges 2", 4, new_array[2])

def test_random_array():
    random.seed(1)
    new_array = a.random_array(1,0,100)
    assert_equals("New array", 17, new_array[0])

def test_random_arrays():
    random.seed(1)
    new_array = a.random_array(3,0,100)
    assert_equals("3 values 0", 17, new_array[0])
    assert_equals("3 values 1", 72, new_array[1])
    assert_equals("3 values 2", 97, new_array[2])

def test_is_sorted():
    random.seed(1)
    empty_array = a.is_sorted(a.range_array(0,0))
    one_element_array = a.is_sorted(a.range_array(0,1,1))
    sorted = a.is_sorted(a.range_array(0,10,2))
    unsorted = a.is_sorted(a.random_array(4, 1, 100))

    assert_equals("empty array true?", True, empty_array)
    assert_equals("one element array sorted true?", True, one_element_array)
    assert_equals("sorted true?", True, sorted)
    assert_equals("unsorted true?", False, unsorted)
    

def run_all_tests():
    #run_test(test_range_array)
    run_test(test_range_arrays)
    #run_test(test_random_array)
    #run_test(test_random_arrays)
    #run_test(test_is_sorted)

run_all_tests()