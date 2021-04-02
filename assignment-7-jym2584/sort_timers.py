''' Plots various sorts functions
'''
import array_utils as a
import sorts as s
import plotter as p
import time
import random

SCALAR = 25
RUNS = 25

def sort_timer(sort_function, an_array):
    '''Calculates the time a specified function sorts with a given array
    '''
    start = time.perf_counter()
    sort_function(an_array)
    end = time.perf_counter()
    timer = end-start
    return timer

def time_sorted(sort_function):
    ''' Plots insertion sort
    '''
    p.init("Insertion Sort", "Length", "Time")
    for i in range(0,RUNS):                         #a.range_array(min, max, step)
        p.add_data_point(sort_timer(sort_function,a.range_array(0,SCALAR+(i*SCALAR))))
    p.plot()

def time_random(sort_function):
    ''' Plots random sort
    '''
    random.seed(1)
    p.init("Random Bubble Sort", "Length", "Time")
    for i in range(0,RUNS):                                     #a.random_array(size, min, max)
        p.add_data_point(sort_timer(sort_function,a.random_array(SCALAR+(i*SCALAR), 0, SCALAR+(i*SCALAR))))
    p.plot()

def time_reverse(sort_function):
    ''' Plots time reverse sort
    '''
    p.init("Reverse Insertion Sort", "Length", "Time")
    for i in range(0,RUNS):                         #a.range_array(min, max, step)
        p.add_data_point(sort_timer(sort_function,a.range_array(SCALAR+(i*SCALAR),0,-1)))
    p.plot()

def plot_all():
    ''' Plots all
    '''
    p.init("Sort Timers (Sorted, Random, Reverse)", "Length", "Time")
    for i in range(0,RUNS):
        p.add_data_point(sort_timer(s.insertion_sort,a.range_array(0,SCALAR+(i*SCALAR))))
    p.new_series()
    for i in range(0,RUNS):
        p.add_data_point(sort_timer(s.bubble_sort,a.random_array(SCALAR+(i*SCALAR), 0, SCALAR+(i*SCALAR))))
    p.new_series()
    for i in range(0,RUNS):
        p.add_data_point(sort_timer(s.insertion_sort,a.range_array(SCALAR+(i*SCALAR),0,-1)))
    p.plot()
    input("press enter to continue...")

def main():
    #time_sorted(s.insertion_sort)
    random.seed(1)
    #time_random(s.bubble_sort)
    #time_reverse(s.insertion_sort)
    plot_all()

main()