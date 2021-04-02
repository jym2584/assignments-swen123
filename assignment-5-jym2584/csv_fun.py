import csv
import re
import math

def open_reader(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        return reader

def find_address(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            print("Name:", line[0],
            "Address:", line[1],
            "Section:", line[2])

def print_first(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for record in reader:
            print(record[0])

def average(filename,column):
    with open(filename) as file:
        next(file)
        reader = csv.reader(file)
        sum = 0
        count = 0
        for record in reader:
            try:
                print(record[column])
                sum += float(record[column])
            except:
                pass
            count += 1
        print("average grade", sum/count)

def find_digits(a_str):
    '''Finds digits
    [0-9]+ includes 0 through 9
    [a1#] - includes a 1 and #
    [a-z] - only alphabet, etc.
    '''
    for match in re.findall("\d\d", a_str): #Can do \d \D \s \S \w \W (regular expressions) before a_str
        print(match)

def coinflip():
    flip = random(1,2)
    print(random)
def main():
    # opener("data/assignment5_2input.txt")
    find_address("data/full_grades_010.csv")
    #print_first("data/full_grades_010.csv")
    #average("data/full_grades_010.csv", 5)
    find_digits("ab123?!")
main()