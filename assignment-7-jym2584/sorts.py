'''SOrts various arrays
'''
import array_utils

def swap(an_array, a, b):
    #a_init = an_array[a]
    #b_init = an_array[b]
    #print("Swapping", a_init, "and", b_init)
    #an_array[a] = b_init
    #an_array[b] = a_init
    
    #Lecture
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp

def increasing_comparator(a,b):
    return a < b

def decreasing_comparator(a,b):
    return a > b

def shift(an_array, index, comparator=increasing_comparator):
    '''swaps until the value is less than its predecessor
    '''
    while index > 0 and comparator(an_array[index], an_array[index-1]):
        swap(an_array, index, index-1)
        index -= 1

def insertion_sort(an_array, comparator=increasing_comparator):
    '''Sorts the array until its in order
    '''
    num = len(an_array)
    #print(an_array)
    for i in range(0,num):
        shift(an_array, i, comparator)
        #print("Sorting", an_array)

def bubble_sort(an_array, comparator=decreasing_comparator):
    '''Swaps the array until its also on order
    '''
    swapped = True
    num = len(an_array)
    while swapped:
        swapped = False
        for index in range(0,num-1):
            i = index
            j = index+1
            if comparator(an_array[i], an_array[j]):
                swapped = True
                swap(an_array, i, j)
def main():
    #an_array = array_utils.range_array(0, 10)
    #print(an_array)
    #swap(an_array,0,9)
    #print(an_array)

    #an_array = array_utils.range_array(10,0,-1)
    #insertion_sort(an_array)
    
    #an_array = array_utils.range_array(0, 10)
    an_array = array_utils.random_array(10,0,10)
    print("An array before", an_array)
    #insertion_sort(an_array)
    bubble_sort(an_array)
    print("An array after", an_array)

if __name__ == "__main__":
    main()
