"""Prints Binary and Trinary Search Times
"""
import searches
import time
import array_utils as a
import plotter

def average_binary_search(an_array):
    ''' Gets the average binary search time
    length: grabs the entire lengh of the array
    total: adds up the values of binary_search
    total / length: gets the average from total
    '''
    length = len(an_array)
    total = 0
    for i in range(length):
        target = an_array[i]
        start = time.perf_counter()
        searches.binary_search(an_array, target)
        end = time.perf_counter()
        total += (end - start)
    return total / length

def plot_average_binary_searches(min_size,max_size,runs=0):
    '''Plots average of binary search
    '''
    an_array = a.range_array(min_size, max_size)
    run = runs+1

    #plotter.init("Binary Search Time", "Length", "Time")

    for _ in range(0,run):
        plotter.add_data_point(average_binary_search(an_array))
    
    #plotter.plot()

def average_trinary_search(an_array):
    ''' Gets the average trinary search time
    length: grabs the entire lengh of the array
    total: adds up the values of trinary_search
    total / length: gets the average from total
    '''
    length = len(an_array)
    total = 0
    for i in range(length):
        target = an_array[i]
        start = time.perf_counter()
        trinary_search(an_array, target)
        end = time.perf_counter()
        total += (end - start)
    return total / length

def plot_average_trinary_searches(min_size,max_size,runs=0):
    '''Plots average of trinary search
    '''
    an_array = a.range_array(min_size, max_size)
    run = runs+1

    #plotter.init("Trinary Search Time", "Length", "Time")

    for _ in range(0,run):
        plotter.add_data_point(average_trinary_search(an_array))
    
    plotter.plot()

def trinary_search(an_array, target, start=None, end=None):
    """Searches a part of an array by a third instead of a half from binary_search
    start and end: grabs starting and ending index of an array
    step: divides start-end by 3

    returns trinary search whenever it finishes searching from the right or left
    """
    if start == None:
        start = 0
    if end == None:
        end = len(an_array) - 1
    
    #Base Case
    if start > end: #If starting value is greater than end value, the wanted value is not in the array
        return None 
    
    step = (end - start ) // 3
    left = start + step
    right = end - step
    if an_array[right] == target:
        return right
    if an_array[left] == target:
        return left


    #print("Midpoint", midpoint)

    if an_array[right] < target:
        start = right + 1
        return trinary_search(an_array, target, start, end)
    elif an_array[left] > target:
        end = left - 1
        return trinary_search(an_array, target, start, end)
    else:
        start = left + 1
        end = right - 1
        return trinary_search(an_array,target,start,end)


def main():
    #plot_average_binary_searches(100,10000,25)
    #an_array = a.range_array(1,10000)
    #target = 1000
    #print("Found value",target," at index", trinary_search(an_array, target))
    plotter.init("Binary and Trinary Search Time", "Length", "Time")
    plot_average_binary_searches(100,10000,25)
    plotter.new_series()
    plot_average_trinary_searches(100,10000,25)
    input("Enter any key to quit...")

main()