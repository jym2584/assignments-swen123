''' Copy and pasted from sorts_test.py to distinguish my quickbubble sort test
'''
from testing import *
import sorts
import array_utils
import random
import quicksort
import arrays
import hybridsort

def test_quickbubble_sort():
    test_array = array_utils.range_array(5,0,-1)
    result = hybridsort.quickbubble_sort(test_array)
    assert_equals("test", "[1, 2, 3, 4, 5]", str(result))

def run_all_tests():
    run_test(test_quickbubble_sort)

run_all_tests()