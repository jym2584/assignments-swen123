'''
Study Diagram for sorting

Time Complexity     Best        Worst       Expected
Linear Search:      N/A         N/A         O(n)
Binary Search:      N/A         N/A         O(logn)
Insertion Sort:     O(n)        O(n^2)      O(n^2)
             If it is sorted   Not sorted

Bubble Sort:        O(n)        O(n^2)      O(n^2)
Merge Sort:         O(nlogn)    O(nlogn)    O(nlogn)
Quick Sort:         O(nlogn)    O(n^2)      O(nlogn)
                                            (Change pivot to middle)

# Binary Sort: 
'''

import math
import arrays as a
import array_utils as au
def is_power(a, b):
    if a == 1:
        return True
    elif a % b != 0:
        return False
    else:
        return is_power (a / b, b)

def what_power(a, b):
    if a == 1:
        return 0
    elif a % b != 0:
        return ValueError("Not a value")
    else:
        return what_power(a / b , b) + 1

def range_array(an_array, start = 0, step = 1, index = 0):
    if index == len(an_array):
        pass
    else:
        an_array[index] = start
        start += step
        index += 1
        range_array(an_array, start, step, index)

def arrays_equal(an_array, an_array2, index = 0):
    if index == len(an_array) and index == len(an_array2):
        return True
    elif index == len(an_array) or index == len(an_array2):
        return False
    elif an_array[index] != an_array2[index]:
        return False
    else:
        return arrays_equal(an_array, an_array2, index + 1)

def tuplify():
    first = input("Enter your first name: ")
    middle = input("Enter your middle name (if applicable): ")
    last = input("Enter your last name: ")

    if middle == "":
        return (first, last)
    else:
        return (first, middle, last)

def cube(a_list):
    for i in range(len(a_list)):
        a_list[i] = a_list[i]**3
    return a_list

def reversal(a_list, index = 0):
    if index == len(a_list):
        return []
    else:
        reversed = reversal(a_list, index + 1)
        reversed.append(a_list[index])
        return reversed

def multiples(rows, columns):
    table = []
    for row in range(rows):
        table.append([])
        for column in range(columns):
            value = (row + 1) * (column + 1)
            table[row] += ["{:2}".format(value)]
    return table

def multiples_2(rows, columns):
    row = []
    column = []
    table = []
    for i in range(rows):
        print()
        for j in range(columns):
            print(i * j , end= " ")

    print(table)
def main():
    #print(is_power(256, 4))
    #print(is_power(15,3))
    #print(what_power(256, 4))
    #$print(what_power(15, 3))
    #an_array = a.Array(10)
    #range_array(an_array, 2, 5)
    #print(an_array)
    #array_copy = an_array
    #an_array3 = a.Array(10)
    #arrays_equal(an_array, array_copy)
    #print(an_array == array_copy)
    #print(arrays_equal(an_array, an_array3))
    
    #print(tuplify())
    #a_list = [1,2,3,4,5]
    #print(cube(a_list))
    #print(reversal(a_list))
    table = multiples(5,5)
    for rows in table:
        print(rows)
    print(table[2][3])
    print(table[2][4])

    #multiples_2(5,5)


if __name__ == "__main__":
    main()