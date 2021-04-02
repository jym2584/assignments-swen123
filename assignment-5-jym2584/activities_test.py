from testing import *
import activities

# TDD example
def test_for_exception():
    #setup
    num = 10
    den = 0
    #invoke
    try:
        activities.division(num, den)
        testing.fail("No exception")
    #analyze
    except ArithmeticError:
        pass

def exponent_test():
    #setup
    base = 2
    power = 4
    #invoke
    result = activities.exponent(base,power)
    #Analyze
    assert_equals("result power", 16, result)

def exponent_test_negative():
    #setup
    base = 2
    power = -4
    #invoke
    try:
        activities.exponent(base,power)
        fail("Exception Expected")
    #analysis
    except ValueError:
        pass

def run_all_tests():
    run_test(exponent_test)
    run_test(exponent_test_negative)

run_all_tests()