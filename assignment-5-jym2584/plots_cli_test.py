import plots_cli as p
import csv
import re
from testing import *

#Step 3
def test_lab_average():
    #Setup
    #Invoke
    average = p.lab_average("data/full_grades_010.csv", "Sion", "Lobasso")
    #Analyze
    assert_floats("Test Lab Average", 72.67, average)

#Step 5
def test_get_average():
    average = p.get_average("data/grades_010.csv", 7)
    average2 = p.get_average("data/grades_010.csv", 4)
    assert_floats("Lab 6", 67.77, average)
    assert_floats("Lab 3", 82.61, average2)

def run_all_tests():
    run_test(test_lab_average)
    run_test(test_get_average)

run_all_tests()