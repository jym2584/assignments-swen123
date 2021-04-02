from quicksort import *
import array
import random
''' Testing for quicksort.py
'''
############ PARTITION TEST ############
def test_partition_sorted(): #  destructively affects the list
    ''' Notes from CA tutoring'''
    #Setup
    #list = 54321, 3 as middle value, 54 on right , 21 on left
    # [5,4,3,2,1]
    #a_list = [1,2,3,4,5] # high is len(a_list) which is also 4
    #low = 0
    #high = len(a_list) - 1
    #expected = 3 # want the middle index
    #return value would be equal to 3
    #Invoke
    # pivot should be 4
    #1,3,5,6,9
    # pivot index would be 5
    
    ''' Actual test code
    Testing if the partition can run without any errors sorted.
    '''
    #Setup
    a_list = [1,2,3,4,5]
    low = 0
    high = len(a_list) - 1
    expected = 4
    
    #Invoke
    actual = partition(a_list, low, high) # returns index of the pivot, everything element smaller than the expected 
    
    #Analyze
    assert expected == actual

# everything smaller than the pivot is on the left, everything bigger than the pivot is on the right

def test_partition_6_lists(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [6,5,4,3,2,1]
    low = 0
    high = len(a_list) - 1
    expected = 0
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual

def test_partition_none(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    a_list = []
    low = 0
    high = len(a_list) - 1
    expected = None

    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual

def test_partition_6_lists(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    a_list = [7,5,2,1,6,8,9,4,3]
    low = 0
    high = len(a_list) - 1
    expected = 2
    
    #Invoke
    actual = partition(a_list, low, high) #everything from 0 to 1 is smaller than index 2, everything from 3 to 7 is bigger than index 2
    
    #Analyze
    assert expected == actual

def test_partition_random():
    a_list = [4, 3, 5, 2, 1, 3, 2, 3]
    low = 0
    high = len(a_list) - 1
    expected = 3

    actual = partition(a_list, low, high)
    assert expected == actual


############ END PARTITION TEST ############

############ PARTITION Mon, Oct 19 ############
def test_partition_3_lists(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [1,2,3]
    low = 0
    high = len(a_list) - 1
    expected = 2
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual

def test_partition_3_lists_random1(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [1,3,2]
    low = 0
    high = len(a_list) - 1
    expected = 1
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual

def test_partition_3_lists_random2(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [3,1,2]
    low = 0
    high = len(a_list) - 1
    expected = 1
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual

def test_partition_3_lists_random3(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [2, 3, 1]
    low = 0
    high = len(a_list) - 1
    expected = 0
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual


def test_partition_3_lists_random3(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [3,2,1]
    low = 0
    high = len(a_list) - 1
    expected = 0
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual


def test_partition_5_lists_random3(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [1,5,3,6,2]
    low = 0
    high = len(a_list) - 1
    expected = 1
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual

def test_partition_5_lists_invalid(): #  destructively affects the list
    '''Testing if the partition can run without any values on the list
    '''
    #Setup
    
    a_list = [1,"not a list", True, 2, 3]
    low = 0
    high = len(a_list) - 1
    expected = None
    
    #Invoke
    actual = partition(a_list, low, high)
    
    #Analyze
    assert expected == actual

############ PARTITION Mon, Oct 19 ############

############ QUICKSORT TEST ############


def test_quicksort():
    a_list = [4, 3, 5, 2, 1, 3, 2, 3]
    expected = [1, 2, 2, 3, 3, 3, 4, 5]

    quicksort(a_list)
    actual = a_list

    assert expected == actual # Pivot differs from the expected (3)
    
def test_quicksort_3lists():
    a_list = [1,3,2]
    expected = [1,2,3]

    quicksort(a_list)
    actual = a_list

    assert expected == actual # Pivot differs from the expected (3)

def test_quicksort_from_main():
    a_list = [4, 3, 5, 2, 1, 3, 2, 3]
    expected = [1, 2, 2, 3, 3, 3, 4, 5]

    quicksort(a_list)
    actual = a_list

    assert expected == actual # Pivot differs from the expected (3)

############ END QUICKSORT TEST ############