import sorts
import time
import array_utils as a
import random
def func_caller(a_func, x):
    print(a_func.__name__)
    result = a_func(x)
    print(result)

def square_it(y):
    return y*y

def double_it(z):
    return z*2

#func_caller(square_it,5)
#func_caller(double_it,2)


def runner(a_func,n):
    print("Running", a_func.__name__)
    result = a_func(n)
    print(result)

def evens(num):
    '''sums and returns all even values from 0 to n
    '''
    total = 0
    for i in range(0,num+1,2):
        total +=i
    return total

def odds(num):
    total = 0
    for i in range(0,num+1): # or for i in range(1,num+1,2)
        if i % 2 != 0:
            total += i
        else:
            pass
    return total


def insertion_sort_timer(an_array):
    start = time.perf_counter()
    sorts.insertion_sort(an_array)
    end = time.perf_counter()
    return end - start    

def main():
    runner(evens,10)                                          
    runner(odds,10)
    random.seed(1)
    an_array = a.range_array(0,2500)
    print("Sorted time =", insertion_sort_timer(an_array))
    
    an_array = a.random_array(2500)
    print("Random time =", insertion_sort_timer(an_array))
    
    an_array = a.range_array(2500,0,-1)
    print("Reversed time =", insertion_sort_timer(an_array))
           
main()