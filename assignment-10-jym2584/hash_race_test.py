from hash_race import *
import random

def test_string_hash_bad():
    ''' Testing for bad hash string using 3 string values, should result in 0 every time.
    '''
    #setup
    string1 = "hello"
    string2 ="hello world"
    string3 = "quizmaker?"
    expected = 0
    #invoke
    actual1 = string_hash_bad(string1)
    actual2 = string_hash_bad(string2)
    actual3 = string_hash_bad(string3)
    #analyze
    assert expected == actual1
    assert expected == actual2
    assert expected == actual3

def test_string_hash_inconsistent():
    ''' Tests random string hash given the same string value
    '''
    #setup
    random.seed(0)
    string1 = "hello"
    string2 = "hello"
    string3 = "hello"
    #invoke
    actual1 = string_hash_inconsistent(string1)
    actual2 = string_hash_inconsistent(string2)
    actual3 = string_hash_inconsistent(string3)
    #analyze
    assert 11988 == actual1
    assert 5439 == actual2
    assert 10767 == actual3

def test_string_hash_ascii():
    ''' Tests ascii test if it adds each character value to the max
    '''
    #setup
    string = "hello"
    expected = 532
    #invoke
    actual = string_hash_ascii(string)
    #analyze
    assert expected == actual

def test_string_hash_better():
    ''' Tests hash code using the equation
    '''
    #setup
    string = "hello"
    expected = 99162322
    #invoke
    actual = string_hash_better(string)
    #analyze
    assert expected == actual

def test_collisions():
    ''' Tests collision bad
    '''
    #setup
    size = 100000
    hash_func = string_hash_bad
    #invoke
    total_collisions, average_collisions = collisions(size, hash_func)
    #analyze
    assert total_collisions == 17575
    assert average_collisions == 17575

def test_collisions_good():
    ''' Tests collision good, should all be 0
    '''
    #setup
    size = 100000
    hash_func = string_hash_better
    #invoke
    total_collisions, average_collisions = collisions(size, hash_func)
    #analyze
    assert total_collisions == 0
    assert average_collisions == 0