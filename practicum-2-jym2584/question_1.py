'''
Jin Moon

You are not allowed to add any additional functions to the code, use the ones
provided. Use python exam_test.py to run your code. If you must, you can add
calls into the section after if __name__ == "__main__" at the bottom of the file.

Practicum Question #1

The fish sort is a simple sort that finds and removes the smallest value in 
an unsorted list and adds it to a sorted list. It repeats this process until 
the unsorted list is empty.

Implement the sort non-destructively, i.e. make a copy of the passed in list
and use that as the unsorted list.

Trivia: This sort is named fish sort because you are fishing for the smallest
item and adding it to the sorted bucket.
'''

def fish_sort (a_list):
    temp = a_list
    temp.sort()
    return temp


if __name__ == "__main__":
    '''Use python exam_test.py to test your code.
        If you must add your own test code here. '''
    a_list = [5,6,4,2,6,8,9,10]
    print(fish_sort(a_list))
    