from testing import *
import sorts
import array_utils
import random
import quicksort
import arrays
import hybridsort

def test_shift():
    #setup
    random.seed(1)
    an_array = array_utils.range_array(10,0,-1)
    an_array_init = array_utils.range_array(10,0,-1)
    index = 3
    print("Array before", an_array)
    #invoke
    sorts.shift(an_array,index,comparator=sorts.increasing_comparator)
    print("Array after", an_array)
    #analyze
    assert an_array[1] != an_array_init[1]

def test_insertion_sort():
    #setup
    random.seed(1)
    an_array = array_utils.range_array(10,0,-1)
    an_array_init = array_utils.range_array(10,0,-1)
    print("Array before", an_array)
    #invoke
    sorts.insertion_sort(an_array, comparator=sorts.increasing_comparator)
    print("Array after", an_array)
    #analyze
    for i in range(0, len(an_array)):
        assert an_array[i] != an_array_init[i]

def test_bubble_sort():
    #setup
    random.seed(1)
    an_array = array_utils.random_array(10,0,10)
    an_array_init = an_array
    print("Array before", an_array)
    #invoke
    sorts.bubble_sort(an_array, comparator=sorts.increasing_comparator)
    print("Array after", an_array)
    #analyze
    for i in range(0, len(an_array)):
        assert an_array[i] == an_array_init[i]

def test_quicksort_empty():
    test_array = arrays.Array(0)
    result = quicksort.quicksort(test_array)
    assert_equals("array", '[]', str(result))

def test_quicksort_reverse():
    test_array = array_utils.range_array(5, 0, -1)
    result = quicksort.quicksort(test_array)
    assert_equals("array", '[1, 2, 3, 4, 5]', str(result))

def test_partition():
    test_array = array_utils.range_array(5,0,-1)
    less, same, more = quicksort.partition(3, test_array)
    assert_equals("less", "[2, 1]", str(less))
    assert_equals("same", "[3]", str(same))
    assert_equals("more", "[5, 4]", str(more))

def test_quickbubble_sort():
    test_array = array_utils.range_array(5,0,-1)
    result = hybridsort.quickbubble_sort(test_array)
    assert_equals("test", "[1, 2, 3, 4, 5]", str(result))

def run_all_tests():
    #run_test(test_shift)
    #run_test(test_insertion_sort)
    #run_test(test_bubble_sort)
    run_test(test_quicksort_empty)
    run_test(test_quicksort_reverse)
    run_test(test_partition)
    run_test(test_quickbubble_sort)

run_all_tests()