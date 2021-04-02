import csv
import arrays
import re

#1
def nameStates(filename, character):
    with open(filename) as file:
        next(file)
        reader = csv.reader(file)
        nameList = []
        for record in reader:
            name = record[0]
            splitName = name.split()
            lastName = splitName[1]
            for letter in lastName:
                if letter.lower() == character.lower():
                    nameList.append(name)
                    break
        arr = arrays.Array(len(nameList))
        for i in range(len(nameList)):
            arr[i] = nameList[i]
        
        return arr

#2
def colorStates(filename, color):
    with open(filename) as file:
        next(file)
        reader = csv.reader(file)
        stateList = []
        for line in reader:
            if color == line[1]:
                line3 = line[3]
                address_broken = line3.split()
                state = address_broken[len(address_broken)-2]
                exists = False
                for i in stateList:
                    if i == state:
                        exists = True
                        print("There is a duplicate", state)
                if not exists:
                    stateList.append(state)
        return stateList

#3
def factorial(n):
    if n < 0:
        raise ValueError("Can't be negative")
    elif n <= 1:
        return 1
    else:
        return n * factorial(n-1)

#4
def palindrome(string):
    length = len(string)
    string = string.upper()
    if length == 1 or length == 0: # If the first letter is the same as the last letter, we can recurse
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        return False

#5
def sumOfValues(a_list):
    #list[1::] means rest of the list
    if len(a_list) == 0:
        return 0
    try:
        len(a_list[0]) # see if this is a list (integer will throw error)
        return sumOfValues(a_list[0]) + sumOfValues(a_list[1::])
    
    except TypeError: # this means if it's an integer
        return a_list[0] + sumOfValues(a_list[1::])

def sumofValues2(a_list):
    '''
    [1,[2,[3],4], 5]
    1  +   9   +  5 
    '''
    for item in a_list: 
        try:
            x = len(item)
            return sumofValues2(x)
            # recursion(current item)
        except:
            return a_list[0] + sumofValues2(a_list[1::])
                    # 1 + recursion(rest of the list)

def squareRoots(num):
    lists = []
    for i in range(1, num+1):
        lists.append(i ** .5)
    return lists

#6.2
def squareRoots_listcomprehension(num):
    return [item ** .5 for item in range(1, num + 1)]

#7
def DotProductof2Lists(list1, list2):
    the_list = []
    for item in list1:
        for item2 in list2:
            the_list += [item + " " + item2]
    return the_list

#8
def valid_email(email):
    if re.findall('[a-z]{3}[a-z]?\d{4}@(g.)?rit.edu', email):
        return True
    else:
        return False

def main():

    #1
    #print(nameStates("Data.csv", "N"))

    #2
    print(colorStates("data.csv", "Orange"))

    #3
    #print(factorial(5))

    #4
    #print(palindrome("racecar"))
    #print(palindrome("test"))

    #6
    #print(squareRoots(16))
    #print(squareRoots_listcomprehension(16))

    #7
    #list1 = ["help", "smell"]
    #list2 = ["yourself", "me"]
    #print(DotProductof2Lists(list1, list2))
    #8
    #print(valid_email("jym2584@rit.edu"))





if __name__ == "__main__":
    main()