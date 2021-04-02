'''
Jin Moon

Function to compute if two arrays are equal to each other.
DO NOT ALTER THIS FUNCTION IN ANY WAY!!!
'''
from array_utils import *

def equal (array1, array2):
    i = 0
    try:
        while i < len (array1) or i < len (array2):
            if array1[i] != array2[i]:
                return False
            else:
                i += 1
    except IndexError:
        return False

    return True

'''
In the space below, write pytest tests that ensure 100% code coverage 
of the equal function. The tests should be located in this file but they 
will be automatically run when executing pytest.

To view the coverage report you can use either of the following commands:
pytest --cov=array_equality --cov-report=term-missing
pytest array_equality.py --cov=array_equality --cov-report=term-missing

Do not forget, your system may need to use
    py -m pytest
or
    python -m pytest
or 
    python3 -m pytest
instead of just 'pytest'.
'''
def test_array_equal():
    #setup
    array = range_array(1, 10)
    array2 = range_array(1, 10)
    
    #invoke
    equal2 = equal(array, array2)
    #assert
    assert True == equal2

def test_array_notequal():
    #setup
    array = random_array(10, 1, 10)
    array2 = range_array(1, 10)
    
    #invoke
    equal2 = equal(array, array2)
    #assert
    assert False == equal2

def test_array_reversed():
    #setup
    array = range_array(1,10, -1)
    array2 = range_array(1, 10)
    
    #invoke
    equal2 = equal(array, array2)
    #assert
    assert False == equal2

if __name__ == '__main__':
    pass
    ''' Your non-test code goes here, if you have any '''