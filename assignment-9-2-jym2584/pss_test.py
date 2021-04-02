from pss import *

def test_dot_product_empty   ():
    # Setup
    matrix_a = []
    matrix_b = []
    expected = []

    # Invoke
    actual = dot_product (matrix_a, matrix_b)

    # Analysis
    assert expected == actual

def test_dot_product_invalid ():
    # Setup
    matrix_a = [[1, 2, 3]]
    matrix_b = [[3, 4, 5]]

    # Invoke
    try:
        dot_product (matrix_a, matrix_b)
        assert False
    
    # Analysis
    except ValueError:
        assert True

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
    assert expected_a_dot_b == actual_ab
    assert expected_b_dot_a == actual_ba

