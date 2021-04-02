'''
DO NOT MODIFY

Testing file for the exam questions. You will not be able to get above a 50% for a given question if none
of the tests pass. Please make sure you do not submit code with syntax errors in it.
'''

from question_1 import *
from question_2 import *
from question_3 import *
from question_4 import *
from question_5 import *
from testing import *
import array_utils
import random

def student_proof (test_function):
    """
    Won't protect against syntax errors
    """
    try:
        run_test (test_function, False) # Change to True to only see one failure at a time
    except Exception as e:
        fail ("Unexpected Exception Encountered - " + type(e).__name__ + ": " + str(e))

NAME_FIELD = ("NAME", 0, 7)
TYPE_FIELD = ("TYPE", 8, 13)
COLOR_FIELD = ("COLOR", 14, 22)
AGE_FIELD = ("AGE", 23, 25)

def test_fish_sort_empty ():
    # Setup
    pond = []
    expected = []

    # Invoke
    barrel = fish_sort (pond)

    # Analysis
    assert_equals ("fish_sort: List", expected, barrel)

def test_fish_sort ():
    # Setup
    pond = random.sample (range (1000), 10)
    expected = sorted (pond)

    # Invoke
    barrel = fish_sort (pond)

    #Analysis
    assert_equals ("fish_sort: List", expected, barrel)

def test_question_1 ():
    test_fish_sort_empty ()
    test_fish_sort ()

def test_get_field_data ():
    record = "Herman  bird  green    27 "
    assert_equals("get_field_data: Name", "Herman", get_field_data (record, NAME_FIELD[1], NAME_FIELD[2]))
    assert_equals("get_field_data: Type", "bird", get_field_data (record, TYPE_FIELD[1], TYPE_FIELD[2]))
    assert_equals("get_field_data: Color", "green", get_field_data (record, COLOR_FIELD[1], COLOR_FIELD[2]))
    assert_equals("get_field_data: Age", "27", get_field_data (record, AGE_FIELD[1], AGE_FIELD[2]))


def test_count_pets ():
    assert_equals("count_pets: Sample Name",1,count_pets("data/sample_pets.txt","NAME","Rascal"))
    assert_equals("count_pets: Sammple Type",2,count_pets("data/sample_pets.txt","TYPE","bird"))
    assert_equals("count_pets: Sample Color",0,count_pets("data/sample_pets.txt","COLOR","yellow"))
    assert_equals("count_pets: Sample Age",1,count_pets("data/sample_pets.txt","AGE","27"))

    assert_equals("count_pets: Name",2,count_pets("data/pets.txt","NAME","Bingo"))
    assert_equals("count_pets: Type",4,count_pets("data/pets.txt","TYPE","bird"))
    assert_equals("count_pets: Color",2,count_pets("data/pets.txt","COLOR","blue"))
    assert_equals("count_pets: Color not found",0,count_pets("data/pets.txt","COLOR","purple"))
    assert_equals("count_pets: Age",1,count_pets("data/pets.txt","AGE","27"))

    assert_none("count_pets: Fail to open", count_pets("data.txt", "NAME", "Rascal"))

def test_question_2 ():
    test_get_field_data ()
    test_count_pets ()

def test_reverse_an_array ():
    # Setup
    array1 = array_utils.range_array(1, 11)
    expected = array_utils.range_array (10, 0, -1)

    # Invoke
    reverse_an_array(array1)

    # Analysis
    assert_equals ("reverse_an_array: Array", str (expected), str (array1))

def test_question_3 ():
    test_reverse_an_array ()

def test_helper_string_to_array(a_string):
    an_array = arrays.Array(len(a_string))
    for i in range(len(a_string)):
        an_array[i] = int(a_string[i])
    return an_array

def bin_to_int_1():
    #setup
    expected_binary = "1"
    #invoke
    actual_int = bin_to_int(test_helper_string_to_array(expected_binary))
    #analyze
    assert_equals("bin_to_int: result",1,actual_int)

def bin_to_int_2():
    #setup
    expected_binary = "0"
    #invoke
    actual_int = bin_to_int(test_helper_string_to_array(expected_binary))
    #analyze
    assert_equals("bin_to_int: result",0,actual_int)

def bin_to_int_3():
    #setup
    expected_binary = "1101"
    #invoke
    actual_int = bin_to_int(test_helper_string_to_array(expected_binary))
    #analyze
    assert_equals("bin_to_int: result",13,actual_int)

def test_question_4 ():
    bin_to_int_1 ()
    bin_to_int_2 ()
    bin_to_int_3 ()

def test_dot_product_empty ():
    # Setup
    matrix_a = []
    matrix_b = []
    expected = []

    # Invoke
    actual = dot_product (matrix_a, matrix_b)

    # Analysis
    assert_equals ("Product", expected, actual)

def test_dot_product_invalid ():
    # Setup
    matrix_a = [[1, 2, 3]]
    matrix_b = [[3, 4, 5]]

    # Invoke
    try:
        dot_product (matrix_a, matrix_b)
        fail ("Exception Expected!")
    
    # Analysis
    except ValueError:
        assert_none ("ValueError", None)

def test_dot_product ():
    # Setup
    matrix_a = [[1, 2, 3]]
    matrix_b = [[4], [5], [6]]
    expected_a_dot_b = [[32]]
    expected_b_dot_a = [[4, 8, 12], [5, 10, 15], [6, 12, 18]]

    # Invoke
    actual_ab = dot_product (matrix_a, matrix_b)
    actual_ba = dot_product (matrix_b, matrix_a)

    # Analysis
    assert_equals ("Product A dot B", expected_a_dot_b, actual_ab)
    assert_equals ("Product B dot A", expected_b_dot_a, actual_ba)

def test_question_5 ():
    test_dot_product_empty ()
    test_dot_product_invalid ()
    test_dot_product ()

def run_all_tests ():
    student_proof (test_question_1)
    student_proof (test_question_2)
    student_proof (test_question_3)
    student_proof (test_question_4)
    student_proof (test_question_5)

run_all_tests ()