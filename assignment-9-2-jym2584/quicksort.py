# Python program for implementation of Quicksort  
  
# This function is same in both iterative and recursive 
def partition (a_list, low, high): 
    if len(a_list) == 0:
        return None
    else:
        try:
            i = low - 1
            pivot = a_list[high]
            #print("pivot", pivot)
        
            for j in range (low, high): 
                if  a_list[j] < pivot: 
        
                    # increment index of smaller element 
                    i = i + 1
                    # swap i and j values
                    temp = a_list[i]
                    a_list[i] = a_list[j]
                    a_list[j] = temp
                    #a_list[j] = a_list[i] 
        
            # swap pivot (index j) into the correct location
            temp = a_list[i + 1]
            a_list[i + 1] = a_list[high]
            a_list[high] = temp
            #a_list[high] = a_list[i + 1]

            # return the pivot index
            return (i + 1) 
        except:
            return None
  
# Function to do Quick sort 
# a_list[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
def quicksort_iter (a_list, low, high): 
  
    # Create an index list
    index_list = []
  
    # push initial values of low and high to index_list 
    index_list.append (low) 
    index_list.append (high) 
    #print("Low", low)
    #print("High", high)
    # Keep popping from index_list while is not empty 
    while index_list != []: 
  
        # Pop high and low 
        high = index_list.pop () 
        low = index_list.pop () 
  
        # Set pivot element at its correct position in 
        # sorted array 
        pivot = partition(a_list, low, high) 
        #print("Pivot", pivot)
        # If there are elements on left side of pivot, 
        # then push left side to index_list 
        if pivot > low: 
            #print("Low", low)
            index_list.append (low) 
            index_list.append (pivot - 1)
  
        # If there are elements on right side of pivot, 
        # then push right side to index_list 
        if pivot < high: 
            #print("High", high)
            index_list.append (pivot + 1)
            index_list.append (high) 

  
def quicksort (a_list):
    quicksort_iter (a_list, 0, len(a_list) - 1)

# Driver code to test above 
def main ():
    a_list = [4, 3, 5, 2, 1, 3, 2, 3]
    #a_list_copy = [4, 3, 5, 2, 1, 3, 2, 3]
    #n = len(a_list) 
    print("The Pivot of a_list is", partition(a_list, 0, len(a_list)-1))
    quicksort (a_list)
    print ("Sorted array is:", a_list)
  
if __name__ == "__main__":
    main ()

# This code is contributed by Mohit Kumra 