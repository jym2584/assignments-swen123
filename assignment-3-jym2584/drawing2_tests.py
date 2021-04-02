import drawing2

def test_get_x(value, expected, id):
    x = drawing2.get_x (value)
    assert(x == expected)
    print("Test Get X,", id, "Passed")

def run_all_tests():
    test_get_x (0, -200, 1)
    test_get_x (400,200, 2)

run_all_tests()