'''
A simple testing module.

@author GCCIS Faculty.
'''

__stop_on_failure = True
__passed = True
__header = ''


def stop_test ():
    if __stop_on_failure:
        exit (1) 
    else: 
        global __passed
        __passed = False

def run_test(test_function, stop_on_failure=True):
    """
    Prints the name of the test function before running it. If the function
    completes without an error, a message is printed to indicate that the
    test passed.

        Parameters:
            test_function: The test function to run. This function must be
                parameterless.
    """
    global __stop_on_failure
    __stop_on_failure = stop_on_failure
    global __passed
    __passed = True
    global __header
    __header = "running " + test_function.__name__ + "... "

    if callable(test_function):
        test_function()
        if __passed:
            print(__header, "passed!", sep='')
    else:
        print("argument to run test is not a function (", test_function, "). ",
            "Make sure you called run_test(test_func) nand ot run_test(test_func()).",
            sep="")
        exit(1)

def assert_true(property_name, actual, print_on_success=False):
    """
    Asserts that the actual value is True. If it is not True, an error message
    is printed and the program exits with an error code. This is a convenience
    function that is equivalent to "assert_equals("name", True, actual)".

        Parameters:
            property_name: The name of the property being tested; used for 
                output.
            actual: The actual value.
            print_on_success: If True, a message is printed if the comparison
                is successful, i.e. expected == actual.
    """
    assert_equals(property_name, True, actual, print_on_success)

def assert_false(property_name, actual, print_on_success=False):
    """
    Asserts that the actual value is False. If it is not False, an error message
    is printed and the program exits with an error code. This is a convenience
    function that is equivalent to "assert_equals("name", False, actual)".

        Parameters:
            property_name: The name of the property being tested; used for 
                output.
            actual: The actual value.
            print_on_success: If True, a message is printed if the comparison
                is successful, i.e. expected == actual.
    """
    assert_equals(property_name, False, actual, print_on_success)

def assert_equals(property_name, expected, actual, print_on_success=False):
    """
    Compares the expected and actual values for equality. If they are unequal,
    an error message is printed and the program exits with an error code.

        Parameters:
            property_name: The name of the property being tested; used for 
                output.
            expected: The expected value.
            actual: The actual value.
            print_on_success: If True, a message is printed if the comparison
                is successful, i.e. expected == actual.
    """
    if expected != actual:
        print (__header, end = ' ')
        print("assertion failed!", property_name, "should be", expected,
          "but was", actual)
        stop_test()
    elif print_on_success:
        print("  ", property_name, "is", expected)


def assert_floats(property_name, expected, actual, threshold=0.05, print_on_success=False):
    """
    Compares the expected and actual floating point values to see if the two
    values are within the specific threshold and therefore considered "close
    enough" to be equivalent. If the two values are outside of the specified
    threshold, an error message is printed and the program exits with an 
    error code.

        Parameters:
            property_name: The name of the property being tested.
            expected: The expected value. Must be int or float.
            actual: The actual value. Must be int or float.
            threshold: The maximum amount by which the two values may differ
                and still be considered to be equivalent. Default value is 
                0.05.
            print_on_success: If True, a message is printed if the comparison
                is successful, i.e. expected and actual are within the 
                threshold of equality.
            
    """
    if not isinstance(expected, (float, int)):
        print (__header, end = ' ')
        print("  assertion failed!", property_name, 
            "expected value is non-numeric:", expected)
        stop_test()
    elif not isinstance(actual, (float, int)):
        print (__header, end = ' ')
        print("  assertion failed!", property_name, 
            "actual value is non-numeric:", actual)
        stop_test()
    elif abs(expected - actual) > threshold:
        print (__header, end = ' ')
        print("  assertion failed!", property_name, "should be", expected,
            "but was", actual)
        stop_test()
    elif print_on_success:
        print("  ", property_name, "is within", threshold, "of", expected)

def assert_none(property_name, value, print_on_success=False):
    """
    Compares the specified value to None. If the value is not None, an error
    message is printed and the program exits with an error code.

        Parameters:
            property_name: The name of the property being tested; used for 
                output.
            value: The value being compared to None.
            print_on_success: If True, a message is printed if the comparison
                is successful, i.e. value is None.

    """
    assert_equals(property_name, None, value, print_on_success)


def assert_not_none(property_name, value, print_on_success=False):
    """
    Asserts that the specified value is not None.

        Parameters:
            property_name: The name of the property being tested; used for
                output.
            value: The value being compared to None.
            print_on_success: If True, a message is printed if the comparison
                is successful, i.e. value is not None.
    """
    if value == None:
        print (__header, end = ' ')
        print("assertion failed!", property_name, "should not be None")
        stop_test()
    elif print_on_success:
        print("  ", property_name, "is not None")

def fail(message):
    """
    Called to automatically fail a test, e.g. when an error is not raised but
    should have been.
    """
    print (__header, end = ' ')
    print("failed!", message)
    stop_test()