""" This is the test file for running plots.py
@author: Jin Moon
"""
import plots as p
from testing import *

def test_lab_average():
    #Setup
    #Invoke
    average = p.lab_average("data/grades_010.csv", "Sion", "Lobasso")
    #Analyze
    assert_floats("Test Lab Average", 80.66, average)

def test_lab_average_DNE():
    average_DNE = p.lab_average("data/grades_010.csv", "ThisStudent", "DoesNotExist")
    assert_none("Does this student exist?", average_DNE)

def test_get_average():
    average = p.get_average("data/grades_010.csv", 7)
    average2 = p.get_average("data/grades_010.csv", 4)
    assert_floats("Lab 6", 67.77, average)
    assert_floats("Lab 3", 82.61, average2)

def test_get_gradeitem():
    grade_item = p.get_average("data/grades_010.csv", 137)
    assert_none("Does this student exist?", grade_item)

def run_all_tests():
    run_test(test_lab_average)
    run_test(test_lab_average_DNE)
    run_test(test_get_average)

run_all_tests()