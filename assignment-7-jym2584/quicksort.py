import arrays
import array_utils as a

def cat(array1,array2):
    new_array = arrays.Array(len(array1)+len(array2))
    for i in range(len(array1)):
        new_array[i] = array1[i]
    for i in range(len(array2)):
        new_array[i + len(array1)] = array2[i]
    
    return new_array

def quicksort(an_array):
    if len(an_array) == 0:
        return an_array
    else:
        pivot = an_array[0]
        less, same, more = partition(pivot, an_array)
        
    new = cat(quicksort(less), same)
    new = cat (new, quicksort(more))
    return new

def partition(pivot, an_array):
    less = arrays.Array(len(an_array))
    same = arrays.Array(len(an_array))
    more = arrays.Array(len(an_array))

    less_index, same_index, more_index = 0,0,0

    for i in range(len(an_array)):
        if an_array[i] < pivot:
            less[less_index] = an_array[i]
            less_index += 1
        elif an_array[i] > pivot:
            more[more_index] = an_array[i]
            more_index += 1
        else:
             same[same_index] = an_array[i]
             same_index += 1

    return a.copy_array(less, less_index), \
           a.copy_array(same, same_index), \
           a.copy_array(more, more_index)

def main():
    #array = create_array("data/random.txt")
    #print(array)
    #print(copy_array(array))
    
    print(cat(arrays.Array(1,2), arrays.Array(1,3)))
    #pass

if __name__ == "__main__":
    main()