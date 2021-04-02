"""
DO NOT MODIFY THIS FILE
In any way!
If you think you need to, PM me to discuss.
"""

from question1 import *
from question2 import *
from question3_4 import *
from question5 import *

# Question 1 Tests
def test_contains_all_true():
    # setup
    a_list = [1, 2, 3, 4, 5]
    b_list = [2, 4, 3]
    expected = True

    # invoke
    actual = contains_all(a_list, b_list)

    # analyze
    assert expected == actual

def test_contains_all_false():
    # setup
    a_list = [1, 2, 3, 4, 5]
    b_list = [1, 2, 5, 4, 3, 6]
    expected = False

    # invoke
    actual = contains_all(a_list, b_list)

    # analyze
    assert expected == actual

# Question 2 Tests
def test_grade_dict():
    #setup
    student_ids = ['mza2757', 'msq3092', 'wbk2202', 'oqg0697', 'epu3058', 'qqf9768', 'kqx0405', 'lba4698', 'wcw3792', 'iaw8916', 'lfa0636', 'ijk9199', 'jvl5932', 'yik8289', 'dpv0398', 'mko9759', 'hlt7616', 'iij5419', 'ehv3921', 'smv5704']
    grades = [96, 57, 86, 65, 89, 63, 75, 67, 65, 51, 98, 53, 71, 78, 87, 96, 89, 63, 82, 63]
    expected = {
        'A': ['mza2757', 'lfa0636', 'mko9759'],
        'B': ['wbk2202', 'epu3058', 'dpv0398', 'hlt7616', 'ehv3921'],
        'C': ['kqx0405', 'jvl5932', 'yik8289'],
        'D': ['oqg0697', 'qqf9768', 'lba4698', 'wcw3792', 'iij5419', 'smv5704'],
        'F': ['msq3092', 'iaw8916', 'ijk9199']
    }
    #invoke
    actual = grade_dict(student_ids,grades)
    #analyze
    assert expected == actual
    
# Question 3 Tests
'''
No tests provided as they are too big of a give-away for
what must be done. You are welcome to add tests to the 
question3_4.py file. They will be run from exam_test or 
you can run them directly useing:
pytest question3_4.py
'''

# Question 4 Tests
def test_pair_stringify ():
    # Setup
    pair = Pair (5, 'z')
    expected = "(5, z)"

    # Invoke
    actual = str (pair)

    # Analysis
    assert expected == actual

def test_pair_set_usage ():
    # Setup
    pair1 = Pair (5, 'z')
    pair2 = Pair (6, 'a')
    pair3 = Pair (5, 'b')

    # Invoke
    test_set = {pair1, pair2, pair3}

    # Analysis
    assert test_set is not None

def test_pair_sorting ():
    # Setup
    pair1 = Pair (5, 'z')
    pair2 = Pair (6, 'a')
    pair3 = Pair (5, 'b')
    expected = [pair3, pair1, pair2]

    test_list = [pair1, pair2, pair3]

    # Invoke
    actual = sorted (test_list)

    # Analysis
    assert expected == actual
