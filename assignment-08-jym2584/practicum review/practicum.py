import csv
import math
def findname_fromlast(filename, letter):
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        print("Finding last name that starts with", letter)
        for line in reader:
            #print(line[0].split()[1][0])
            if str(line[0].split()[1][0]) == letter:  # Grabbing first column, splitting it which creates First, Last. Grabbing the first index (last name) and the first character of the last name
                print(line[0])
            #print(line[0].split()[1])

def findstate_fromcolor(filename, color):
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        print("States that likes the color", color)
        for line in reader:
            #print(line[1])
            #print(line[3].split("\n")[1].split(", ")[1].split()[0])
            if color == line[1]:
                print(line[3].split("\n")[1].split(", ")[1].split()[0])

def factorial(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return number * factorial(number-1)

def palindrome(string):
    if string == 0:
        return 1
    elif len(string) < len(string):
        return 1
    if string == string[::-1]:
        print("BRO ITS A PALINDROME")
        return palindrome(string)
    else:
        print("Nawh bro, not a palindrome")
        return False

def square_roots(n):
    for i in range(n):
        print(i**(1/2))

def main():
    #findname_fromlast("data.csv", "R")
    #findstate_fromcolor("data.csv", "Orange")
    #print(factorial(5))
    #print(palindrome("ava"))
    square_roots(16)
main()