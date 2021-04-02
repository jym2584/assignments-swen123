from practice14_2 import *

def test_divisible_3_5():
    #setup
    n = 20
    expected = [3, 5, 6, 9, 10, 12, 15, 18, 20]
    #invoke
    actual = divisible_3_5(n)
    #assert
    expected == actual

def test_find_words():
    #setup
    filename = "data/atotc.txt"
    number = 5

    expected_a = ['a', 'anyone', 'anywhere', 'at', 'and']
    expected_d = ['dickens', 'date:', 'disappointment', 'delicacy', 'days']
    expected_h = ['hundreds', 'head', 'honest', 'hand', 'hope,']
    expected_j = ['january,', 'january', 'judith', 'jackal', 'jaw']
    expected_t = ['the', 'tale', 'two', 'this', 'terms']
    expected_x = ['x', 'xi', 'xii', 'xiii', 'xiv']
    expected_z = ['zealous', None, None, None, None]
    #invoke
    actual_a = find_words(filename, "a", number)
    actual_d = find_words(filename, "d", number)
    actual_h = find_words(filename, "h", number)
    actual_j = find_words(filename, "j", number)
    actual_t = find_words(filename, "t", number)
    actual_x = find_words(filename, "x", number)
    actual_z =find_words(filename, "z", number)
    #assert
    assert str(actual_a) == str(expected_a)
    assert str(actual_d) == str(expected_d)
    assert str(actual_h) == str(expected_h)
    assert str(actual_j) == str(expected_j)
    assert str(actual_t) == str(expected_t)
    assert str(actual_x) == str(expected_x)
    assert str(actual_z) == str(expected_z)


def test_calendar():
    #setup
    weekday = 2
    days = 31

    calendar = calendar_month(weekday, days)

    assert calendar[0][2] == "01"
    assert calendar[4][4] == "31"