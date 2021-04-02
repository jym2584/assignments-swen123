from testing import *
import sorts
import arrays
import array_utils as a
import random
import merge_sort

def test_merge_sort_one():
    #setup
    test_array = arrays.Array(1,5)
    
    #invoke
    result = merge_sort.merge_sort(test_array)
    
    #Analysis
    assert_equals("Array", "[5]", str(result))

def test_merge_sort_reverse():
    #setup
    test_array = a.range_array(5,0,-1)
    
    #invoke
    result = merge_sort.merge_sort(test_array)
    
    #Analysis
    assert_equals("Array", "[1, 2, 3, 4, 5]", str(result))

def test_split():
    #setup
    test_array = a.range_array(1,6)

    #invoke
    half1, half2 = merge_sort.split(test_array)

    #analysis
    assert_equals("half1", "[1, 3, 5]", str(half1))
    assert_equals("half2", "[2, 4]", str(half2))


def run_all_tests():
    run_test(test_split)
    run_test(test_merge_sort_one)
    run_test(test_merge_sort_reverse)

run_all_tests()