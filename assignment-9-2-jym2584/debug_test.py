from debug import *

def test_sum():
    #SSetup
    a_list = [1,2,3,4,5]
    expected = 15
    #invoke
    actual = sum(a_list)

    #Analysis
    assert expected == actual

def test_fib():
    #setup
    num = 5
    expected = 5
    #invoke
    actual = fib(num, 0, 1)
    #assert
    assert expected == actual