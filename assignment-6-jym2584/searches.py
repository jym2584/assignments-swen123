import array_utils
import time
import arrays
import random

def linear_search(an_array, target):
    #loop over all indexes
    for i in range(len(an_array)):
    #if value at index matches target, return index
        if an_array[i] == target:
            return i
    #If not found, return none
    return None

def linear_search_timer(an_array, target):
    start = time.perf_counter()
    linear_search(an_array,target)
    stop = time.perf_counter()
    return stop - start

def linear_timer():
    an_array = array_utils.range_array(1,10000000)
    print("Search time =", linear_search_timer(an_array,1))
    print("Search time =", linear_search_timer(an_array,5000000))
    print("Search time =", linear_search_timer(an_array,9999999))

def binary_search_timer(an_array, target):
    start = time.perf_counter()
    binary_search(an_array,target)
    stop = time.perf_counter()
    return stop - start
    
def binear_timer():
    an_array = array_utils.range_array(1,10000000)
    print("Search time =", binary_search_timer(an_array,1))
    print("Search time =", binary_search_timer(an_array,5000000))
    print("Search time =", binary_search_timer(an_array,9999999))

def binary_search(an_array, target, start=None, end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(an_array) - 1
    
    #Base Case
    if start > end: #If starting value is greater than end value, the wanted value is not in the array
        return None 
    
    midpoint = (start + end) // 2
    value = an_array[midpoint]
    #print("Midpoint", midpoint)
    if target == value:
        return midpoint
    elif target < value:
        return binary_search(an_array, target, start, midpoint-1)
    else:
        return binary_search(an_array, target, midpoint + 1, end)




def main():
    an_array = array_utils.range_array(1,100)
    target = 50
    print("Found value",target," at index", binary_search(an_array, target))
    binear_timer()
    #print("Linear search:",linear_search(an_array, 50))
    #linear_timer()

if __name__ == "__main__":
    main()