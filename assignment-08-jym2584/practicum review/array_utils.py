"""
This is a utils file for arrays
"""
import arrays
import random
import time
import searches

def range_array(start, stop, step = 1):
    """Creates a range
    Arguments
    start: the starting point or number
    stop: ending point
    step: how many increiments should we go from start to stop

    Functions and variables
    a_range - defining the range from start stop step arguments
    new_array - creating the array based on a_range
    new_array[i] = a_range[i] - inputting the range values onto the array
    return new_array - returning the array values from our a_range variable
    """
    a_range = range(start,stop,step)
    #print("variable a_range =",a_range)  # Test print statement
    #print("len a_range", len(a_range))   # Test print statement
    #Create a array of the same size as range
    new_array = arrays.Array(len(a_range))
    #print("variable new_array =", new_array)   # Test print statement
    #Copy range elements to array
    for i in range(len(new_array)):
        new_array[i] = a_range[i]
    #Return 
    #print("variable new_array after for loop", new_array)   # Test print statement
    return new_array
        
def randomnum():
    print("Random number:")
    for _ in range(25):
        number = random.randint(1,100)
        print(number,end=" ")
    print("\n")

def roll_dice(how_many_times = 1):
    for i in range(how_many_times):
        number = random.randint(1,6)
        print("Rolling dice", number, ("Times,", i))
    return number

def roll_the_dice(sides):
    return random.randint(1,sides)

def random_seed():
    print("Random seed")
    random.seed(1)
    for _ in range(10):
        number = random.randint(1,100)
        print(number,end=" ")

def random_array(size, min = 0, max = None):
    '''Randomly generates arrays
    Arguments
    size: how many arrays we want
    min: the minimum #
    max: The max, otherwise if none then we set it equal to size

    Functions and Variables
    new_array - generates the array based on size
    random.randint - we randomly generate each array from min to max
    return new_array - we return the new_array values
    '''
    #random.seed(1)
    if max == None:
        max = size
    #create array of size size
    new_array = arrays.Array(size)
    #print(new_array)   # Test print statement
    #fill array with random ints from min - max
    for i in range(size):
        new_array[i] = random.randint(min,max)
    #return array
    #print("variable new_array after for loop", new_array)   # Test print statement
    return new_array

def is_sorted(an_array): 
    '''checks if the array is sorted
    '''
    length = len(an_array)
    if length <= 1:
        return True

    for i in range(1, len(an_array)):
        if an_array[i] < an_array[i-1]:
            return False

    return True

def shuffle(an_array):
    '''
    Shuffles an array and swaps it with another
    '''
    length = len(an_array)
    for i in range(0, length): #Swapping array at i with array at some index
        j = random.randint(0,length-1)
        print(j)
        array_temp = an_array[i]
        an_array[i] = an_array[j]
        an_array[j] = array_temp

    print(an_array)

def timer():
    begin = time.perf_counter()
    sum = 0
    for number in range(1000000000):
        sum += number
    end = time.perf_counter()
    elapsed = end - begin
    print("Time elapsed:", elapsed)

def main():
    #Call range with various values
    #Print out resulting array
    #array1 = range_array(1,10, 2)
    #print("Array 1 =",array1,"\n")

    #array2 = range_array(5,101,5)
    #print("Array 2 =",array2,"\n")

    #array3 = range_array(10,-1,-1)
    #print("Array 3 =",array3,"\n")


    #array1 = random_array(4, 1, 100)
    #print("Array Random 1 =",array1,"\n")

    #array2 = random_array(5,101,5)
    #print("Array 2 =",array2,"\n")

    #array3 = random_array(10,-1,-1)
    #print("Array 3 =",array3,"\n")

    #array3 = is_sorted(array1)
    #print("Is sorted array", array3)

    an_array = range_array(5,101,5)
    print("Shuffled array", shuffle(an_array),"\n")

    #randomnum()

    #roll_dice(10)

    ######Lecture
    #random.seed(1) #Used to write a test for the program if the random num generator runs correctly
    #for _ in range(10):
       #print("(Lecture) Rolled a", roll_the_dice(6))

    #random_seed()

if __name__ == "__main__":
    main()