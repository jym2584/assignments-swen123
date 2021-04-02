import arrays
import array_utils as a
import sorts as s
import quicksort as q
import random
import merge_sort as m

def quickbubble_sort(an_array):
    ''' Uses bubble sort and quicksort
    '''
    if len(an_array) < 10:
        s.bubble_sort(an_array)
        return an_array
    else:
        pivot = an_array[0]
        less, same, more = q.partition(pivot, an_array)
        new_array = q.cat(quickbubble_sort(less), same)
        new_array = q.cat(new_array, quickbubble_sort(more))
        return new_array

def mergesertion_sort(an_array):
    ''' Uses bubble sort and quicksort
    '''
    if len(an_array) < 10:
        m.merge_sort(an_array)
        return an_array
    else:
        for i in range(0,len(an_array)):
            s.shift(an_array, i, s.increasing_comparator)
        return an_array

def mergesertion_sort2(an_array):
    ''' Uses bubble sort and quicksort
    '''
    for i in range(0,len(an_array)):
        s.shift(an_array, i, s.increasing_comparator)
    m.merge_sort(an_array)
    return an_array

def main():
    random.seed(1)
    an_array = a.random_array(10,0,10)
    print("Array before", an_array)
    print("Quickbubble Sort", quickbubble_sort(an_array))
    an_array2 = a.random_array(15,0,10)
    print("Mergesertion Sort", mergesertion_sort2(an_array2))
    
if __name__ == "__main__":
    main()