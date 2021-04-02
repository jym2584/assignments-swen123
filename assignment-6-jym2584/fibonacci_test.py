import fibonacci
from testing import *

def test_fibonacci_naive():
    #setup
    n = 9
    expected = 21
    #invoke
    actual = fibonacci.fibonacci_naive(n)
    #analyze
    assert_equals("fibonacci 9", expected, actual)

def test_fibonacci_fast():
    n = 100
    expected = 218922995834555169026
    actual = fibonacci.fibonacci_fast(n)
    assert_equals("Fibonacci 100", expected, actual)

def run_all_tests():
    run_test(test_fibonacci_naive)
    run_test(test_fibonacci_fast)

run_all_tests()
